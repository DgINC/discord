import datetime
from contextlib import AsyncContextDecorator
from typing import Optional, ClassVar, NoReturn, Any, Union, Callable, Type

import orjson
from aiohttp import ClientSession, BasicAuth, web
from aiohttp.abc import Application
from aiohttp.typedefs import JSONEncoder, StrOrURL

from core.api.configs import OAuthConfigInterface
from core.api.oauth import OAuth2SessionInterface
from core.oauth2 import OAuth2
from core.utils.base import make_trace_config
from discord.core import API_ENDPOINT, API_ENDPOINT_GATEWAY
from discord.core.objects.types.base import HttpMethod


class DiscordSession(AsyncContextDecorator):
    _base_url: ClassVar[StrOrURL] = None
    _auth: ClassVar[OAuth2] = OAuth2
    _oauth_session: ClassVar[Type[OAuth2SessionInterface]] = None
    _config: ClassVar[Type[OAuthConfigInterface]] = None
    _json_serialize: ClassVar[JSONEncoder] = lambda x: orjson.dumps(x,
                                                                    default=lambda obj: obj.isoformat() if isinstance(obj, (datetime.date, datetime.datetime)) else TypeError,
                                                                    option=orjson.OPT_PASSTHROUGH_DATETIME).decode()
    _client: ClassVar[ClientSession] = None
    _ws_client: ClassVar[ClientSession] = None
    _server: ClassVar[Application] = None

    def __init__(self, base_url: StrOrURL = None,
                 config: Optional[Type[OAuthConfigInterface]] = None,
                 oauth_session: Optional[Type[OAuth2SessionInterface]] = None):

        self.trace_config = make_trace_config('Fuck')
        self._base_url = base_url
        self._config = config
        self._oauth_session = oauth_session

    async def __aenter__(self):
        self._server = web.Application()
        self._client = ClientSession(base_url=API_ENDPOINT,
                                     auth=self._auth(self._config, self._oauth_session),
                                     trace_configs=self.trace_config,
                                     json_serialize=self._json_serialize)
        self._ws_client = ClientSession(base_url=self._base_url, json_serialize=self._json_serialize)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.close()
        await self._server.cleanup()
        return False

    async def start_ws(self):
        await self._ws_client.ws_connect(url=API_ENDPOINT_GATEWAY)

    async def close_ws(self):
        for ws in self._ws_client.values():
            if ws:
                await ws.close()

    async def send_request(self, method: HttpMethod, req: str, data: Optional[bytes] = None, **kwargs: Any) -> dict:
        result: dict
        status: int

        async with self._client.request(method=method, url=req, data=data, **kwargs) as resp:
            result = await resp.json(loads=orjson.loads)
            status = resp.status
        return result

    async def close(self) -> NoReturn:
        await self._client.close()

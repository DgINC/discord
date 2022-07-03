from __future__ import annotations
import datetime
from typing import Optional, ClassVar, Any, Type, NoReturn

import orjson
from aiohttp import ClientSession, web, ClientConnectorError
from aiohttp.abc import Application
from aiohttp.typedefs import JSONEncoder, StrOrURL

from discord.core import API_ENDPOINT_GATEWAY
from discord.core.api.configs import OAuthConfigInterface
from discord.core.auth import Auth
from discord.core.objects.types import HttpMethod
from discord.core.utils import make_trace_config


class DiscordSession(object):
    """
    DiscordSession
    """
    _base_url: ClassVar[Optional[StrOrURL]] = None
    _auth: ClassVar[Auth] = None
    _config: ClassVar[Type[OAuthConfigInterface]] = None
    _json_serialize: ClassVar[JSONEncoder] = lambda x: orjson.dumps(x,
                                                                    default=lambda obj: obj.isoformat() if isinstance(
                                                                        obj, (datetime.date,
                                                                              datetime.datetime)) else TypeError,
                                                                    option=orjson.OPT_PASSTHROUGH_DATETIME).decode()
    _client: ClassVar[ClientSession] = None
    _ws_client: ClassVar[ClientSession] = None
    _server: ClassVar[Application] = None

    def __init__(self, base_url: StrOrURL = None,
                 config: Type[OAuthConfigInterface] = None,
                 **kwargs):

        self.trace_config = make_trace_config('Fuck')
        self._base_url = base_url
        self._auth = Auth
        self._config = config

    async def __aenter__(self) -> DiscordSession:
        self._server = web.Application()
        self._client = ClientSession(base_url=self._base_url,
                                     auth=self._auth(self._config),
                                     trace_configs=[self.trace_config],
                                     json_serialize=self._json_serialize)
        self._ws_client = ClientSession(base_url=self._base_url, json_serialize=self._json_serialize)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._server.cleanup()
        return False

    async def start_ws(self):
        await self._ws_client.ws_connect(url=API_ENDPOINT_GATEWAY)

    async def close_ws(self):
        for ws in self._ws_client.values():
            if ws:
                await ws.close()

    async def send_request(self, method: HttpMethod, request: str, data: Optional[bytes] = None, **kwargs: Any) -> dict:
        """

        :param method:
        :param request:
        :param data:
        :param kwargs:
        :return:
        """
        result: dict
        status: int

        params: dict = {}

        for k in kwargs:
            if kwargs[k]:
                params[str(k)].append(str(kwargs[k]))

        try:
            async with self._client.request(method=method, url=request, data=data, params=params) as resp:
                if not resp.status == 200:
                    raise Exception(f"Fetch failed {resp.status}")

                result = await resp.json(loads=orjson.loads)
                status = resp.status
        except ClientConnectorError as e:
            print('Connection Error', str(e))

        return result

    async def close(self) -> NoReturn:
        """
        Close Client Session
        :return: NoReturn
        """
        if not self._client.closed:
            await self._client.close()

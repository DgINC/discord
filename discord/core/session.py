from typing import Optional, ClassVar
import oauthlib

import orjson
from aiohttp import ClientSession, BasicAuth, ClientRequest, web
from aiohttp.abc import Application
from aiohttp.typedefs import JSONEncoder, StrOrURL

from discord.core import API_ENDPOINT, API_ENDPOINT_GATEWAY


class Oauth2(BasicAuth):
    def __init__(
            self,
            client_id=None,
            client=None,
            auto_refresh_url=None,
            auto_refresh_kwargs=None,
            scope=None,
            redirect_uri=None,
            token=None,
            state=None,
            token_updater=None,
            **kwargs
    ):
        pass

    def encode(self) -> str:
        """Encode credentials."""
        return "Barer %s"


class OAuth(ClientRequest):
    pass


class DiscordSession:
    _base_url: Optional[StrOrURL] = API_ENDPOINT
    _auth: Optional[BasicAuth] = None
    _json_serialize: ClassVar[JSONEncoder] = lambda x: orjson.dumps(x).decode()
    _client: ClassVar[ClientSession] = None
    _ws_client: ClassVar[ClientSession] = None
    _server: ClassVar[Application] = None

    def __init__(self):
        self._server = web.Application()
        self._client = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)
        self._ws_client = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)

    async def start_ws(self):
        await self._ws_client.ws_connect(url=API_ENDPOINT_GATEWAY)

    async def close_ws(self):
        for ws in self._ws_client.values():
            if ws:
                await ws.close()

    async def send_req(self, ):
        await self._client.put()

    async def close(self) -> None:
        return await self._client.close()

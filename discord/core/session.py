import asyncio
from contextlib import asynccontextmanager
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
        pass

    async def __aenter__(self):
        self._server = web.Application()
        self._client = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)
        self._ws_client = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.close()
        await self._server.cleanup()
        pass

    async def start_ws(self):
        await self._ws_client.ws_connect(url=API_ENDPOINT_GATEWAY)

    async def close_ws(self):
        for ws in self._ws_client.values():
            if ws:
                await ws.close()

    async def send_req(self, method: str, req: str, data: Optional[bytes]):
        match method:
            case "get":
                async with self._client.get(url=req) as resp:
                    print(resp.status)
                    print(await resp.text())
            case "put":
                async with self._client.put(url=req, data=data) as resp:
                    print(resp.status)
                    print(await resp.text())

    async def close(self) -> None:
        return await self._client.close()


@asynccontextmanager
async def manager():
    client = DiscordSession()
    try:
        yield client
    finally:
        await client.close()

@manager
async def main():
    pass


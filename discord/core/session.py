from typing import Optional, ClassVar

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
    _base_url: ClassVar[StrOrURL] = API_ENDPOINT
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

    async def send_req(self, method: str, req: str, data: bytes):
        match method:
            case "get":
                async with self._client.get(url=req) as resp:
                    print(resp.status)
                    print(await resp.text())
            case "put":
                async with self._client.put(url=req, data=data) as resp:
                    print(resp.status)
                    print(await resp.text())
            case "delete":
                async with self._client.delete(url=req) as resp:
                    pass
            case "head":
                async with self._client.head(url=req) as  resp:
                    pass
            case "options":
                async with self._client.options(url=req) as resp:
                    pass
            case "patch":
                async with self._client.patch(url=req, data=data) as resp:
                    pass

    async def close(self) -> None:
        return await self._client.close()

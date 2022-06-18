import datetime
from contextlib import AsyncContextDecorator
from typing import Optional, ClassVar, NoReturn

import orjson
from aiohttp import ClientSession, BasicAuth, web
from aiohttp.abc import Application
from aiohttp.typedefs import JSONEncoder, StrOrURL

from discord.core import API_ENDPOINT, API_ENDPOINT_GATEWAY
from discord.core.objects.types.base import HttpMethod


def default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError


class DiscordSession(AsyncContextDecorator):
    _base_url: ClassVar[StrOrURL] = API_ENDPOINT
    _auth: Optional[BasicAuth] = None
    _json_serialize: ClassVar[JSONEncoder] = lambda x: orjson.dumps(x, default=default, option=orjson.OPT_PASSTHROUGH_DATETIME).decode()
    _client: ClassVar[ClientSession] = None
    _ws_client: ClassVar[ClientSession] = None
    _server: ClassVar[Application] = None
        
    def __init__(self, auth: Optional[BasicAuth] = None):
        self._auth = auth

    async def __aenter__(self):
        self._server = web.Application()
        self._client = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)
        self._ws_client = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.close()
        await self._server.cleanup()

    async def start_ws(self):
        await self._ws_client.ws_connect(url=API_ENDPOINT_GATEWAY)

    async def close_ws(self):
        for ws in self._ws_client.values():
            if ws:
                await ws.close()

    async def send_req(self, method: HttpMethod, req: str, data: Optional[bytes] = None) -> dict:
        result: dict
        status: int

        async with self._client.request(method=method, url=req) as resp:
            result = await resp.json(loads=orjson.loads)
            status = resp.status
        return result

    async def close(self) -> NoReturn:
        await self._client.close()

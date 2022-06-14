from typing import Optional, ClassVar, NoReturn, Union

import orjson
from aiohttp import ClientSession, BasicAuth, ClientRequest, web
from aiohttp.abc import Application
from aiohttp.typedefs import JSONEncoder, StrOrURL
from contextlib import AsyncContextDecorator

from pydantic import json

from discord.core import API_ENDPOINT, API_ENDPOINT_GATEWAY
from discord.core.oauth2 import OAuth2
from discord.core.utils.base import METH


class DiscordSession(AsyncContextDecorator):
    _base_url: ClassVar[StrOrURL] = API_ENDPOINT
    _auth: Optional[OAuth2] = None
    _json_serialize: ClassVar[JSONEncoder] = lambda x: orjson.dumps(x).decode()
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
        pass

    async def start_ws(self):
        await self._ws_client.ws_connect(url=API_ENDPOINT_GATEWAY)

    async def close_ws(self):
        for ws in self._ws_client.values():
            if ws:
                await ws.close()

    async def send_req(self, method: METH, req: str, data: bytes) -> json:
        match method:
            case METH.GET:
                async with self._client.get(url=req) as resp:
                    res: json = await resp.json()
                    return res
            case METH.POST:
                async with self._client.post(url=req) as resp:
                    res: json = await resp.json()
                    return res
            case METH.PUT:
                async with self._client.put(url=req, data=data) as resp:
                    res: json = await resp.json()
                    return res
            case METH.DELETE:
                async with self._client.delete(url=req) as resp:
                    res: json = await resp.json()
                    return res
            case METH.HEAD:
                async with self._client.head(url=req) as resp:
                    res: json = await resp.json()
                    return res
            case METH.OPTIONS:
                async with self._client.options(url=req) as resp:
                    res: json = await resp.json()
                    return res
            case METH.PATCH:
                async with self._client.patch(url=req, data=data) as resp:
                    res: json = await resp.json()
                    return res

    async def close(self) -> NoReturn:
        await self._client.close()

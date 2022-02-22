from collections import namedtuple
from typing import Optional, ClassVar

import uvloop as uvloop
from aiohttp import ClientSession, BasicAuth
import asyncio
import orjson
from aiohttp.typedefs import JSONEncoder, StrOrURL
from pydantic import AnyUrl
from pydantic.json import pydantic_encoder

from discord.core.api import API_ENDPOINT


class Oauth2(namedtuple("Oauth2", ["client_id", "password", "encoding"])):
    pass


class DiscordSession:
    _base_url: Optional[StrOrURL] = API_ENDPOINT
    _auth: Optional[BasicAuth] = None
    _json_serialize: JSONEncoder = lambda x: orjson.dumps(x).decode()
    _session: ClassVar[ClientSession] = None

    def __init__(self):
        self._session = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)


async def start():
    st = DiscordSession()

if __name__ == "__main__":
    async def main():
        await start()

    main()

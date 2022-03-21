from typing import Optional, ClassVar
import oauthlib

import orjson
from aiohttp import ClientSession, BasicAuth, ClientRequest
from aiohttp.typedefs import JSONEncoder, StrOrURL

from discord.core import API_ENDPOINT


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
    _json_serialize: JSONEncoder = lambda x: orjson.dumps(x).decode()
    _session: ClassVar[ClientSession] = None

    def __init__(self):
        self._session = ClientSession(base_url=self._base_url, auth=self._auth, json_serialize=self._json_serialize)

    async def start_ws(self):
        await self._session.ws_connect()

    async def send_req(self, ):
        await self._session.put()

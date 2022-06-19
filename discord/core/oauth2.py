from contextlib import AsyncContextDecorator
from random import randrange
from typing import ClassVar

from aiohttp import ClientSession, BasicAuth
from oauthlib.oauth2 import WebApplicationClient

from core import OAUTH_AUTHORIZE
from core.api.configs import SessionConfigInterface
from core.objects.oauth2.base import DiscordScope
from core.utils.base import POST


class OAuth2(BasicAuth, AsyncContextDecorator):
    _client: ClassVar[ClientSession] = None
    _oauth: ClassVar[WebApplicationClient] = None
    _config: ClassVar[SessionConfigInterface] = None

    def __init__(self, config: SessionConfigInterface):
        self._client = ClientSession()
        self._oauth = WebApplicationClient(config.client_id)
        self._config = config

    async def __aenter__(self, config: SessionConfigInterface):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return False

    async def authorization_code_grant(self, scopes: list[DiscordScope], **kwargs):
        code_verifer: str = self._oauth.create_code_verifier(randrange(43, 128))
        req: str = self._oauth.prepare_request_uri(OAUTH_AUTHORIZE,
                                              redirect_uri=self._config.redirect_uri,
                                              scope=scopes,
                                              code_challenge=code_verifer,
                                              code_challenge_method='S256',
                                              state='ffff'
                                              )
        if 'bot' in scopes:
            pass
        self._oauth
        async with self._client.request(method=POST, url=req) as resp:
            print(resp.status)
            print(await resp.text())

    def encode(self) -> str:
        """Encode credentials."""
        return "Bearer %s"

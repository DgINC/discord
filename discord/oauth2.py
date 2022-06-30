from random import randrange
from typing import ClassVar, Optional, Type

import exrex
from aiohttp.abc import Application
from oauthlib.oauth2 import WebApplicationClient

from core import OAUTH_AUTHORIZE
from core.api.configs import OAuthConfigInterface
from core.api.oauth import OAuth2SessionInterface
from core.objects.oauth2.base import DiscordScope
from core.session import DiscordSession
from core.utils.base import POST


class OAuth2(DiscordSession):
    _server: ClassVar[Application] = None
    _oauth: ClassVar[WebApplicationClient] = None
    _config: ClassVar[Type[OAuthConfigInterface]] = None
    _oauth_session: ClassVar[Type[OAuth2SessionInterface]] = None

    def __init__(self,
                 config: Optional[Type[OAuthConfigInterface]] = None,
                 oauth_session: Optional[Type[OAuth2SessionInterface]] = None,
                 server: Optional[Application] = None,
                 **kwargs):
        super(OAuth2, self).__init__(config, **kwargs)

        self._oauth = WebApplicationClient(self._config.client_id)
        self._config = config
        self._server = server
        self._oauth_session = oauth_session

    async def __aenter__(self):
        await super(OAuth2, self).__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super(OAuth2, self).__aexit__(exc_type, exc_val, exc_tb)
        return False

    async def authorization_code_grant(self, scopes: list[DiscordScope], **kwargs):
        self._oauth_session.code_verifier = self._oauth.create_code_verifier(randrange(43, 128))
        self._oauth_session.code_challenge = self._oauth.create_code_challenge(self._oauth_session.code_verifier,
                                                                               'S256')

        self._oauth_session.state = exrex.getone('[a-zA-Z0-9]{9}')

        req: str = self._oauth.prepare_request_uri(OAUTH_AUTHORIZE,
                                                   redirect_uri=self._config.redirect_uri,
                                                   scope=scopes,
                                                   code_challenge=self._oauth_session.code_verifier,
                                                   code_challenge_method='S256',
                                                   state=self._oauth_session.state,
                                                   **kwargs
                                                   )
        response: dict = await self.send_request(method=POST, request=req)
        print(response)

import exrex
from random import randrange
from typing import ClassVar, Type, Optional

from aiohttp import ClientSession, BasicAuth
from oauthlib.oauth2 import WebApplicationClient

from core import OAUTH_AUTHORIZE
from core.api.configs import OAuthConfigInterface
from core.api.oauth import OAuth2SessionInterface
from core.objects.oauth2.base import DiscordScope
from core.utils.base import POST


class OAuth2Base:
    _client: ClassVar[ClientSession] = None
    _server: ClassVar[Application] = Application
    _oauth: ClassVar[WebApplicationClient] = None
    _config: ClassVar[Type[OAuthConfigInterface]] = None
    _oauth_session: ClassVar[Type[OAuth2SessionInterface]] = None

    def __init__(self,
                 config: Optional[Type[OAuthConfigInterface]] = None,
                 oauth_session: Optional[Type[OAuth2SessionInterface]] = None,
                 **kwargs):
        self._client = ClientSession()
        self._oauth = WebApplicationClient(self._config.client_id)
        self._config = config
        self._oauth_session = oauth_session
        super(OAuth2Base, self).__init__()

    async def authorization_code_grant(self, scopes: list[DiscordScope], **kwargs):
        self._oauth_session.code_verifier = self._oauth.create_code_verifier(randrange(43, 128))
        self._oauth_session.code_challenge = self._oauth.create_code_challenge(self._oauth_session.code_verifier, 'S256')

        self._oauth_session.state = exrex.getone('[a-zA-Z0-9]{9}')

        req: str = self._oauth.prepare_request_uri(OAUTH_AUTHORIZE,
                                        redirect_uri=self._config.redirect_uri,
                                        scope=scopes,
                                        code_challenge=self._oauth_session.code_verifier,
                                        code_challenge_method='S256',
                                        state=self._oauth_session.state,
                                        **kwargs
                                        )
        async with self._client.request(method=POST, url=req) as resp:
            print(resp.status)
            print(await resp.text())


class OAuth2(BasicAuth):
    _config: ClassVar[Optional[Type[OAuthConfigInterface]]] = None

    def __init__(self,
                 config: Optional[Type[OAuthConfigInterface]] = None,
                 oauth_session: Optional[Type[OAuth2SessionInterface]] = None,
                 **kwargs):
        super(OAuth2, self).__init__(config=config, oauth_session=oauth_session, **kwargs)
        self._config = config

    def encode(self) -> str:
        """Encode credentials. 'Bearer %s'"""
        return f'Bearer {self._confi,g.credentials}'

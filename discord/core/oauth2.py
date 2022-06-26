from random import randrange
from typing import ClassVar, Type, Optional

from aiohttp import ClientSession, BasicAuth
from oauthlib.oauth2 import WebApplicationClient

from core import OAUTH_AUTHORIZE
from core.api.configs import OAuthConfigInterface
from core.objects.oauth2.base import DiscordScope
from core.utils.base import POST


class OAuth2Base(BasicAuth):
    _client: ClassVar[ClientSession] = None
    _oauth: ClassVar[WebApplicationClient] = None
    _config: ClassVar[Type[OAuthConfigInterface]] = None

    def __init__(self, config: Optional[Type[OAuthConfigInterface]] = None):
        self._client = ClientSession()
        self._oauth = WebApplicationClient(self._config.client_id)
        self._config = config
        super().__init__()

    def __new__(cls, *args, **kwargs) -> "OAuth2Base":
        return super().__new__(cls, *args, **kwargs)

    async def authorization_code_grant(self, scopes: list[DiscordScope], **kwargs):
        code_verifier: str = self._oauth.create_code_verifier(randrange(43, 128))

        if 'bot' in scopes and "permission" not in kwargs:
            raise SyntaxError
        else:
            pass

        self._oauth.prepare_request_uri(OAUTH_AUTHORIZE,
                                        redirect_uri=self._config.redirect_uri,
                                        scope=scopes,
                                        code_challenge=code_verifier,
                                        code_challenge_method='S256',
                                        **kwargs
                                        )
        async with self._client.request(method=POST, url=req) as resp:
            print(resp.status)
            print(await resp.text())


class OAuth2(OAuth2Base):
    _credentials: ClassVar[str] = None
    _config: ClassVar[Optional[Type[OAuthConfigInterface]]] = None

    def __init__(self, config: Optional[Type[OAuthConfigInterface]] = None):
        super().__init__(config)
        self._config = config

    def encode(self) -> str:
        """Encode credentials. 'Bearer %s'"""
        return f'Bearer {self._config.credentials}'

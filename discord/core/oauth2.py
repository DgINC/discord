from abc import ABC, abstractmethod

import aiohttp
from aiohttp import ClientSession, ClientResponse, BasicAuth, ClientRequest

from core import LOGIN_OAUTH_ACCESS_TOKEN
from core.api.configs import SessionConfigInterface
from core.objects.oauth2.base import DiscordScope


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(self, websession: ClientSession, host: str):
        """Initialize the auth."""
        self.websession = websession
        self.host = host

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(self, method, url, **kwargs) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        access_token = await self.async_get_access_token()
        headers["authorization"] = f"Bearer {access_token}"

        return await self.websession.request(
            method, f"{self.host}/{url}", **kwargs, headers=headers,
        )


class Auth(AbstractAuth):
    def __init__(self, websession: ClientSession, host: str, token_manager):
        """Initialize the auth."""
        super().__init__(websession, host)
        self.token_manager = token_manager

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
        if self.token_manager.is_token_valid():
            return self.token_manager.access_token

        await self.token_manager.fetch_access_token()
        await self.token_manager.save_access_token()

        return self.token_manager.access_token


class OAuth2(BasicAuth):
    def __init__(
            self,
            client_id=None,
            client=None,
            scope=None,
            redirect_uri=None,
            token=None,
            state=None,
            **kwargs
    ):
        pass

    def encode(self) -> str:
        """Encode credentials."""
        return (f"Bearer %s" % TOKEN)


class OAuth(BasicAuth):
    def __init__(self, config: SessionConfigInterface, scope: DiscordScope):
        pass

    async def __aenter__(self, config: SessionConfigInterface):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def main(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(LOGIN_OAUTH_ACCESS_TOKEN) as resp:
                print(resp.status)
                print(await resp.text())

    def encode(self) -> str:
        """Encode credentials."""
        return "Bearer %s"

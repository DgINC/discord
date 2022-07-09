from typing import Type, Optional

from aiohttp import BasicAuth

from discord.core.api.configs import OAuthConfigInterface


class Auth(BasicAuth):
    """
    Auth
    """

    def __init__(self, config: Optional[Type[OAuthConfigInterface]] = None, **kwargs):
        super(Auth, self).__init__(**kwargs)
        self._config = config

    def __new__(cls, *args, **kwargs):
        return super(Auth, cls).__new__(cls, login="user", password="123")  # Class BasicAuth piece of shit!

    def encode(self) -> str:
        """

        :return:
        """
        return f'Bearer {self._config.credentials}'

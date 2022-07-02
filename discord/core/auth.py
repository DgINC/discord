from typing import ClassVar, Type, Optional

from aiohttp import BasicAuth

from discord.core.api.configs import OAuthConfigInterface


class Auth(BasicAuth):
    """
    Auth
    """
    _config: ClassVar[Optional[Type[OAuthConfigInterface]]] = None

    def __init__(self, config: Optional[Type[OAuthConfigInterface]] = None, **kwargs):
        super(Auth, self).__init__(**kwargs)
        self._config = config

    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def encode(cls) -> str:
        """

        :return:
        """
        return f'Bearer {cls._config.credentials}'

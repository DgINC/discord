from typing import ClassVar, Type, Optional

from aiohttp import BasicAuth

from core.api.configs import OAuthConfigInterface


class Auth(BasicAuth):
    """
    Auth
    """
    _config: ClassVar[Optional[Type[OAuthConfigInterface]]] = None

    def __init__(self, config: Optional[Type[OAuthConfigInterface]] = None, **kwargs):
        super(Auth, self).__init__(**kwargs)
        self._config = config

    def encode(self) -> str:
        """

        :return:
        """
        return f'Bearer {self._config.credentials}'

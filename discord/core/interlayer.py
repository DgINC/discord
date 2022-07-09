from typing import Optional, Type

from discord.core.api import OAuthConfigInterface
from discord.core.session import DiscordSession


class Interlayer(DiscordSession):
    """
    Interalayer
    """

    def __init__(self, config: Optional[Type[OAuthConfigInterface]] = None, **kwargs):
        super(Interlayer, self).__init__(config, **kwargs)

    async def __aenter__(self):
        await super(Interlayer, self).__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super(Interlayer, self).__aexit__(exc_type, exc_val, exc_tb)

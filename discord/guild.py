from __future__ import annotations

from typing import Type, Optional, Dict

from discord.core import API_ENDPOINT
from discord.core.api.configs import OAuthConfigInterface
from discord.core.exceptions import SessionError
from discord.core.objects.guild import GuildObject, GuildPreviewObject
from discord.core.session import DiscordSession
from discord.core.utils import GET


class Guild(DiscordSession):
    """
    Guild
    """
    guild_id: int = None
    version: int = None

    def __init__(self,
                 guild_id: int,
                 version: int,
                 config: Optional[Type[OAuthConfigInterface]] = None,
                 **kwargs):
        super(Guild, self).__init__(self._base_url, config, **kwargs)
        self._base_url = API_ENDPOINT
        self.guild_id = guild_id
        self._config = config
        self.version = version

    async def __aenter__(self) -> "Guild":
        await super(Guild, self).__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super(Guild, self).__aexit__(exc_type, exc_val, exc_tb)
        return False

    async def create(self, obj: GuildObject) -> GuildObject:  # POST
        pass

    async def get(self, with_counts: bool = False) -> GuildObject:  # GET
        """

        :param with_counts:
        :return:
        """
        resp: Dict = {}

        try:
            resp = await self.send_request(GET,
                                           f"/api/v{self.version}/guilds/{self.guild_id}",
                                           with_counts=with_counts)
        except SessionError as exc:
            pass

        return GuildObject(**resp)

    async def get_preview(self) -> "GuildPreviewObject":  # GET
        pass

    async def modify(self):  # POST
        pass

    async def delete(self):  # DELETE
        pass

    async def get_channels(self):  # GET
        pass

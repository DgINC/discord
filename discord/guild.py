from typing import Type

from discord.core.api.configs import OAuthConfigInterface
from discord.core import API_ENDPOINT
from discord.core.objects.guildobjects import GuildObject, GuildPreviewObject
from discord.core.session import DiscordSession
from discord.core.utils.base import GET


class Guild(DiscordSession):
    guild_id: int
    version: int

    def __init__(self,
                 guild_id: int,
                 config: Type[OAuthConfigInterface] = None):
        self._base_url = API_ENDPOINT
        super(Guild, self).__init__(self._base_url, config)
        self.guild_id = guild_id
        self._config = config

    async def __aenter__(self) -> "Guild":
        await super(Guild, self).__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super(Guild, self).__aexit__(exc_type, exc_val, exc_tb)
        return False

    async def create(self, data: tuple) -> GuildObject:  # POST
        pass

    async def get(self, with_counts: bool = False) -> GuildObject:  # GET
        resp: dict = await self.send_request(GET,
                                             f"/api/v{self.version}/guilds/{self.guild_id}",
                                             with_counts=with_counts)
        return GuildObject(**resp)

    async def get_preview(self) -> GuildPreviewObject:  # GET
        pass

    async def modify(self):  # POST
        pass

    async def delete(self):  # DELETE
        pass

    async def get_channels(self):  # GET
        pass

from typing import ClassVar, Type

from core import API_ENDPOINT
from core.api.configs import OAuthConfigInterface
from discord.core.objects.guildobjects import GuildObject, GuildPreviewObject
from discord.core.session import DiscordSession
from discord.core.utils.base import GET


class Guild:
    _client: ClassVar[DiscordSession]
    _config: ClassVar[Type[OAuthConfigInterface]]
    guild_id: int
    version: int

    def __init__(self, guild_id: int, config: Type[OAuthConfigInterface]):
        self.guild_id = guild_id
        self._config = config

    async def __aenter__(self):
        self._client = DiscordSession(base_url=API_ENDPOINT, config=self._config)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def create(self, data: tuple) -> GuildObject:  # POST
        pass

    async def get(self, with_counts: bool = False) -> GuildObject:  # GET
        async with self._client.send_request(GET,
                                             f"/api/v{self.version}/guilds/{self.guild_id}",
                                             with_counts=with_counts) as resp:
            pass

    async def get_preview(self) -> GuildPreviewObject:  # GET
        pass

    async def modify(self):  # POST
        pass

    async def delete(self):  # DELETE
        pass

    async def get_channels(self):  # GET
        pass

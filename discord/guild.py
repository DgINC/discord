import asyncio
from typing import ClassVar

from discord.core.objects.guildobject import GuildObject
from discord.core.session import DiscordSession
from discord.utils.base import METH


class Guild:
    _client: ClassVar[DiscordSession]
    guild_id: int

    def __init__(self, guild_id: int):
        self.guild_id = guild_id

    def __aiter__(self):
        return self

    async def __aenter__(self):
        self._client = DiscordSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def create(self, data: tuple) -> GuildObject:  # POST
        pass

    async def get(self, with_counts: bool = False) -> GuildObject:   # GET
        async with self._client.send_req(METH.GET, f"/api/v9/guilds/{self.guild_id}") as resp:
            pass

    async def get_preview(self):   # GET
        pass

    async def modify(self):    # POST
        pass

    async def delete(self):    # DELETE
        pass

    async def get_channels(self):  # GET
        pass


async def main():
    try:
        async with Guild(12356) as G:
            await G.get()
    finally:
        pass

asyncio.run(main())

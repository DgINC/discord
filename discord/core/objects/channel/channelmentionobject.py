from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

if TYPE_CHECKING:
    from discord.core.objects import BaseObject
    from discord.core.objects.channel import ChannelType
    from discord.core.objects.types import ChannelID, GuildID


@dataclass
class ChannelMentionObject(BaseObject):
    """
    ChannelMention
    """
    id: ChannelID
    guild_id: GuildID
    type: ChannelType
    name: str

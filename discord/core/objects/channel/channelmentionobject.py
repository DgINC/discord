from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

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

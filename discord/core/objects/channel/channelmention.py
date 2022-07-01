from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.channel import ChannelType
from core.objects.types import ChannelID, GuildID


@dataclass
class ChannelMention(BaseObject):
    """
    ChannelMention
    """
    id: ChannelID
    guild_id: GuildID
    type: ChannelType
    name: str

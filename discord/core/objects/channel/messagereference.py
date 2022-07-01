from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.types import MessageID, ChannelID, GuildID


@dataclass
class MessageReference(BaseObject):
    """
    MessageReference
    """
    message_id: MessageID
    channel_id: ChannelID
    guild_id: GuildID
    fail_if_not_exists: bool

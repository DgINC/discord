from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import MessageID, ChannelID, GuildID


@dataclass
class MessageReferenceObject(BaseObject):
    """
    MessageReferenceObject
    """
    message_id: MessageID
    channel_id: ChannelID
    guild_id: GuildID
    fail_if_not_exists: bool

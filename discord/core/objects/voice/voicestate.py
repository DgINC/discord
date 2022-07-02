from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.guild import GuildMemberObject
    from discord.core.objects.types import GuildID, ChannelID, UserID


@dataclass
class VoiceStateObject(BaseObject):
    """
    VoiceStateObject
    """
    guild_id: GuildID
    channel_id: ChannelID
    user_id: UserID
    member: GuildMemberObject
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: bool
    self_video: bool
    suppress: bool
    request_to_speak_timestamp: int

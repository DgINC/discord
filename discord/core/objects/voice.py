from dataclasses import dataclass

from .types.snowflake import GuildID, OwnerID, AppID, ChannelID, UserID
from .base import BaseObject
from .guild import GuildMember


@dataclass
class VoiceState(BaseObject):
    guild_id: GuildID
    channel_id: ChannelID
    user_id: UserID
    member: GuildMember
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: bool
    self_video: bool
    suppress: bool
    request_to_speak_timestamp: int

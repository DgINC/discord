from dataclasses import dataclass

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.channel import ChannelID
from discord.core.objects.guildobjects import GuildID, GuildMemberObject
from discord.core.objects.user import UserID


@dataclass
class VoiceState(BaseObject):
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


@dataclass
class VoiceRegion(BaseObject):
    id: str
    name: str
    optional: bool
    deprecated: bool
    custom: bool

from dataclasses import dataclass, field
from enum import IntEnum
from typing import List

from .types.snowflake import SnowFlake, GuildID, MessageID, AppID, UserID, ChannelID
from .base import BaseObject


class ChannelType(IntEnum):
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_STORE = 6
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13


class VideoQualityMode(IntEnum):
    AUTO = 1
    FULL = 2


@dataclass
class Overwrite(BaseObject):
    id: UserID
    type: int
    allow: str
    deny: str


@dataclass
class Channel(BaseObject):
    id: ChannelID
    type: ChannelType
    guild_id: GuildID
    position: int
    permission_overwrites: List[Overwrite] = field(default_factory=List)

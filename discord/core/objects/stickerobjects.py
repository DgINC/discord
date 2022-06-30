from dataclasses import dataclass
from enum import IntEnum
from typing import TypeVar

from discord.core.objects.user import User

from discord.core.objects.guildobjects import GuildID

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.types.snowflake import SnowFlake

StickerID = TypeVar('StickerID', bound=SnowFlake)


class StickerType(IntEnum):
    STANDARD = 1
    GUILD = 2


class StickerFormatType(IntEnum):
    PNG = 1
    APNG = 2
    LOTTIE = 3


@dataclass
class StickerItem(BaseObject):
    id: StickerID
    name: str
    format_type: StickerFormatType


@dataclass
class StickerObject(BaseObject):
    id: StickerID
    pack_id: StickerID
    name: str
    description: str
    tags: str
    asset: str
    type: StickerType
    format_type: StickerFormatType
    available: bool
    guild_id: GuildID
    user: User
    sort_value: int

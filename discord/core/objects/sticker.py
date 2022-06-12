from dataclasses import dataclass
from enum import IntEnum
from typing import TypeVar

from .base import BaseObject
from .guildobject import GuildID
from .types.snowflake import SnowFlake
from .user import User

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
class Sticker(BaseObject):
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


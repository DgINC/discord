from dataclasses import dataclass
from enum import IntEnum

from discord.core.objects.types.base import StickerID, GuildID
from discord.core.objects.user import User
from discord.core.objects.baseobject import BaseObject


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

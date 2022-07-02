from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.sticker import StickerType, StickerFormatType
from core.objects.types import StickerID, GuildID
from core.objects.user import UserObject


@dataclass
class StickerObject(BaseObject):
    """
    StickerObject
    """
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
    user: UserObject
    sort_value: int

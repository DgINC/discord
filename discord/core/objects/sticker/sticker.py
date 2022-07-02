from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.sticker import StickerType, StickerFormatType
    from discord.core.objects.types import StickerID, GuildID
    from discord.core.objects.user import UserObject


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

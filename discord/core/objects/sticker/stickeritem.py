from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.sticker import StickerFormatType
    from discord.core.objects.types import StickerID


@dataclass
class StickerItemObject(BaseObject):
    """
    StickerItem
    """
    id: StickerID
    name: str
    format_type: StickerFormatType

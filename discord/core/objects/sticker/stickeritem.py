from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.sticker import StickerFormatType
from core.objects.types import StickerID


@dataclass
class StickerItemObject(BaseObject):
    """
    StickerItem
    """
    id: StickerID
    name: str
    format_type: StickerFormatType

__all__ = [
    "StickerType",
    "StickerFormatType",
    "StickerObject",
    "StickerItemObject"
]

from enum import IntEnum
from typing import final, Final

from core.objects.sticker.sticker import StickerObject
from core.objects.sticker.stickeritem import StickerItemObject


@final
class StickerType(IntEnum):
    """
    StickerType
    """
    STANDARD: Final = 1
    GUILD: Final = 2


@final
class StickerFormatType(IntEnum):
    """
    StickerFormatType
    """
    PNG: Final = 1
    APNG: Final = 2
    LOTTIE: Final = 3

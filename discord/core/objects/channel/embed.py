from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.channel import EmbedType, EmbedFooterObject, EmbedImageObject, EmbedThumbnailObject, \
        EmbedVideoObject, EmbedProviderObject, EmbedAuthorObject, EmbedFieldObject


@dataclass
class EmbedObject(BaseObject):
    """
    EmbedObject
    """
    title: str
    type: EmbedType
    description: str
    url: str
    timestamp: int
    color: int
    footer: EmbedFooterObject
    image: EmbedImageObject
    thumbnail: EmbedThumbnailObject
    video: EmbedVideoObject
    provider: EmbedProviderObject
    author: EmbedAuthorObject
    fields: list[EmbedFieldObject] = field(default_factory=list)

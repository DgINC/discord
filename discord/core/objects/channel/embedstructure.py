from dataclasses import dataclass, field

from core.objects import BaseObject
from core.objects.channel import EmbedType, EmbedImage, EmbedThumbnail, EmbedVideo
from core.objects.channel.embedauthor import EmbedAuthor
from core.objects.channel.embedfield import EmbedField
from core.objects.channel.embedfooter import EmbedFooter
from core.objects.channel.embedprovider import EmbedProvider


@dataclass
class EmbedStructure(BaseObject):    # TODO: Find out the correct name of the object
    """
    Embed
    """
    url: str
    proxy_url: str
    height: int
    width: int


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
    footer: EmbedFooter
    image: EmbedImage
    thumbnail: EmbedThumbnail
    video: EmbedVideo
    provider: EmbedProvider
    author: EmbedAuthor
    fields: list[EmbedField] = field(default_factory=list)

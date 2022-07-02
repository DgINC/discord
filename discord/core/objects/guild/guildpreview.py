from dataclasses import dataclass

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.emojis import Emoji
from discord.core.objects.guild import GuildFutures
from discord.core.objects.stickerobjects import StickerObject
from discord.core.objects.types.base import GuildID


@dataclass
class GuildPreviewObject(BaseObject):
    """
    GuildPreviewObject
    """
    id: GuildID
    name: str
    icon: str
    splash: str
    discovery_splash: str
    emojis: list[Emoji]
    features: list[GuildFutures]
    approximate_member_count: int
    approximate_presence_count: int
    description: str
    stickers: list[StickerObject]

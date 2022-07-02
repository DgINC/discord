from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.emojis import EmojiObject
    from discord.core.objects.guild import GuildFutures
    from discord.core.objects.sticker import StickerObject
    from discord.core.objects.types import GuildID


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
    emojis: list[EmojiObject]
    features: list[GuildFutures]
    approximate_member_count: int
    approximate_presence_count: int
    description: str
    stickers: list[StickerObject]

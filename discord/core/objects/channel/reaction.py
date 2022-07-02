from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject
if TYPE_CHECKING:
    from discord.core.objects.emojis import EmojiObject


@dataclass
class ReactionObject(BaseObject):
    """
    ReactionObject
    """
    count: int
    me: bool
    emoji: EmojiObject

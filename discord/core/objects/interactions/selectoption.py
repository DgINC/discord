from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.emojis import EmojiObject


@dataclass
class SelectOptionObject(BaseObject):
    """
    SelectOptionObject
    """
    label: str
    value: str
    description: str
    emoji: EmojiObject
    default: bool

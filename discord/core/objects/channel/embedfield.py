from __future__ import annotations
from dataclasses import dataclass

from discord.core.objects import BaseObject


@dataclass
class EmbedFieldObject(BaseObject):
    """
    EmbedField
    """
    name: str
    value: str
    inline: bool

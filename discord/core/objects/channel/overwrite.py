from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import UserID


@dataclass
class OverwriteObject(BaseObject):
    """
    Overwrite
    """
    id: UserID
    type: int
    allow: str
    deny: str

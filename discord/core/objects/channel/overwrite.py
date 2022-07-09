from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

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

from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.role import RoleObject
    from discord.core.objects.types import EmojiID
    from discord.core.objects.user import UserObject


@dataclass
class EmojiObject(BaseObject):
    """
    EmojiObject
    """
    id: EmojiID
    name: str
    roles: list[RoleObject]
    user: UserObject
    require_colons: bool
    managed: bool
    animated: bool

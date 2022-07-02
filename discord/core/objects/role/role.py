from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.role.roletags import RoleTagsObject
    from discord.core.objects.types import RoleID


@dataclass
class RoleObject(BaseObject):
    """
    RoleObject
    """
    id: RoleID
    name: str
    color: int
    hoist: bool
    icon: str
    unicode_emoji: str
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: RoleTagsObject

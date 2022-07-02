from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.role.roletags import RoleTagsObject
from core.objects.types import RoleID


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

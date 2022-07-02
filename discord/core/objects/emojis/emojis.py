from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.role import RoleObject
from core.objects.types import EmojiID
from core.objects.user import UserObject


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

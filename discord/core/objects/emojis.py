from dataclasses import dataclass
from typing import List

from .types.snowflake import EmojiID
from .role import Role
from .user import User
from .base import BaseObject


@dataclass
class Emoji(BaseObject):
    id: EmojiID
    name: str
    roles: List[Role]
    user: User
    require_colons: bool
    managed: bool
    animated: bool

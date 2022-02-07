from dataclasses import dataclass
from typing import TypeVar

from .types.snowflake import SnowFlake
from .role import Role
from .user import User
from .base import BaseObject

EmojiID = TypeVar('EmojiID', bound=SnowFlake)


@dataclass
class Emoji(BaseObject):
    id: EmojiID
    name: str
    roles: list[Role]
    user: User
    require_colons: bool
    managed: bool
    animated: bool

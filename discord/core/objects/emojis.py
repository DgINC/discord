from dataclasses import dataclass
from typing import TypeVar

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.role import Role
from discord.core.objects.types.snowflake import SnowFlake
from discord.core.objects.user import User

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

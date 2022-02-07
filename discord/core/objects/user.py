from dataclasses import dataclass
from typing import TypeVar

from .types.snowflake import SnowFlake
from .base import BaseObject

UserID = TypeVar('UserID', bound=SnowFlake)


@dataclass
class User(BaseObject):
    id: UserID
    username: str
    discriminator: str
    avatar: str
    verified: bool
    email: str
    flags: int
    banner: str
    accent_color: int
    premium_type: int
    public_flags: int

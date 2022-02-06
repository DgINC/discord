from dataclasses import dataclass
from .types.snowflake import UserID
from .base import BaseObject


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

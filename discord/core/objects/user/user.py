from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.types import UserID


@dataclass
class UserObject(BaseObject):
    """
    UserObject
    """
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

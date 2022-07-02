from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import UserID


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

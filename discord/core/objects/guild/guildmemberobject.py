from dataclasses import dataclass

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.types.base import RoleID
from discord.core.objects.user import User


@dataclass
class GuildMemberObject(BaseObject):
    """
    GuildMemberObject
    """
    user: User
    nick: str
    avatar: str
    roles: list[RoleID]
    joined_at: int
    premium_since: int
    deaf: bool
    mute: bool
    pending: bool
    permissions: str
    communication_disabled_until: int

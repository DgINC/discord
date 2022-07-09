from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import RoleID
    from discord.core.objects.user import UserObject


@dataclass
class GuildMemberObject(BaseObject):
    """
    GuildMemberObject
    """
    user: UserObject
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

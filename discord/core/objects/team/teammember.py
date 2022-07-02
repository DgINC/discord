from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import SnowFlake
    from discord.core.objects.user import UserObject


@dataclass
class TeamMemberObject(BaseObject):
    """
    TeamMemberObject
    """
    membership_state: int
    permissions: list[str]
    team_id: SnowFlake
    user: UserObject

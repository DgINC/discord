from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.team import TeamMemberObject
    from discord.core.objects.types import SnowFlake


@dataclass
class TeamObject(BaseObject):
    """
    TeamObject
    """
    icon: str
    id: SnowFlake
    members: list[TeamMemberObject]
    name: str
    owner_user_id: SnowFlake

from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.team import TeamMemberObject
from core.objects.types import SnowFlake


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

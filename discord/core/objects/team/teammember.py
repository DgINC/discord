from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.types import SnowFlake
from core.objects.user import UserObject


@dataclass
class TeamMemberObject(BaseObject):
    """
    TeamMemberObject
    """
    membership_state: int
    permissions: list[str]
    team_id: SnowFlake
    user: UserObject

from dataclasses import dataclass

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.types.snowflake import SnowFlake
from discord.core.objects.user import User


@dataclass
class TeamMember(BaseObject):
    membership_state: int
    permissions: list[str]
    team_id: SnowFlake
    user: User


@dataclass
class Team(BaseObject):
    icon: str
    id: SnowFlake
    members: list[TeamMember]
    name: str
    owner_user_id: SnowFlake

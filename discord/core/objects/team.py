from dataclasses import dataclass

from pydantic import BaseModel

from .types.snowflake import SnowFlake
from .user import User
from .base import BaseObject


@dataclass
class TeamMember(BaseModel):
    membership_state: int
    permissions: list[str]
    team_id: SnowFlake
    user: User


@dataclass
class Team(BaseModel):
    icon: str
    id: SnowFlake
    members: list[TeamMember]
    name: str
    owner_user_id: SnowFlake

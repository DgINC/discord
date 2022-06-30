from dataclasses import dataclass
from typing import TypeVar

from discord.core.objects.baseobject import BaseObject
from discord.core.objects.types.snowflake import SnowFlake, BotID, IntegrID

RoleID = TypeVar('RoleID', bound=SnowFlake)


@dataclass
class RoleTags(BaseObject):
    bot_it: BotID
    integration_id: IntegrID
    premium_subscriber: None


@dataclass
class Role(BaseObject):
    id: RoleID
    name: str
    color: int
    hoist: bool
    icon: str
    unicode_emoji: str
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: RoleTags

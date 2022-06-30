from dataclasses import dataclass
from enum import IntFlag
from typing import TypeVar, final

from core.objects.baseobject import BaseObject
from discord.core.objects.team import Team
from discord.core.objects.types.snowflake import SnowFlake
from discord.core.objects.user import User

ApplicationID = TypeVar('ApplicationID', bound=SnowFlake)


@final
class ApplicationFlag(IntFlag):
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17
    GATEWAY_MESSAGE_CONTENT = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED = 1 << 19


@dataclass
class ApplicationObject(BaseObject):
    id: ApplicationID
    name: str
    icon: str
    description: str
    rpc_origins: list[str]
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: str
    privacy_policy_url: str
    owner: User
    summary: str
    verify_key: str
    team: Team
    guild_id: SnowFlake
    primary_sku_id: SnowFlake
    slug: str
    cover_image: str
    flags: ApplicationFlag

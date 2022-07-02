from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.team import TeamObject
from core.objects.types import ApplicationID, GuildID, SnowFlake
from core.objects.user import UserObject
from discord.core.objects.application import ApplicationFlag


@dataclass
class ApplicationObject(BaseObject):
    """
    ApplicationObject
    """
    id: ApplicationID
    name: str
    icon: str
    description: str
    rpc_origins: list[str]
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: str
    privacy_policy_url: str
    owner: UserObject
    summary: str
    verify_key: str
    team: TeamObject
    guild_id: GuildID
    primary_sku_id: SnowFlake
    slug: str
    cover_image: str
    flags: ApplicationFlag
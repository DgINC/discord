from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from discord.core.objects import BaseObject
    from discord.core.objects.team import TeamObject
    from discord.core.objects.types import ApplicationID, GuildID, GenericID
    from discord.core.objects.user import UserObject
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
    primary_sku_id: GenericID
    slug: str
    cover_image: str
    flags: ApplicationFlag

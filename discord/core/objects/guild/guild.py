from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import Field
from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.channel import ChannelObject
    from discord.core.objects.emojis import EmojiObject
    from discord.core.objects.guild import VerificationLevel, MessageNotificationLevel, MFALevel, \
        ExplicitContentFilterLevel, SystemChannelFlags, GuildMemberObject, GuildFutures
    from discord.core.objects.role import RoleObject
    from discord.core.objects.types import GuildID, UserID, ApplicationID, ChannelID
    from discord.core.objects.voice import VoiceStateObject


@dataclass
class GuildObject(BaseObject):
    """
    GuildObject
    """
    id: GuildID
    name: str
    icon: str
    icon_hash: str
    splash: str
    description: str
    emojis: list[EmojiObject]
    banner: str
    owner: bool
    owner_id: UserID
    permissions: str
    application_id: ApplicationID
    afk_channel_id: ChannelID
    afk_timeout: int
    system_channel_id: ChannelID
    widget_enabled: bool
    verification_level: VerificationLevel
    roles: list[RoleObject]
    default_message_notifications: MessageNotificationLevel
    mfa_level: MFALevel
    explicit_content_filter: ExplicitContentFilterLevel
    max_presences: int
    max_members: int
    vanity_url_code: str
    premium_tier: int
    premium_subscription_count: int
    system_channel_flags: SystemChannelFlags
    preferred_locale: str
    rules_channel_id: ChannelID
    public_updates_channel_id: ChannelID
    joined_at: int
    large: bool
    unavailable: bool
    member_count: int
    channels: list[ChannelObject]
    threads: list[ChannelObject]
    nsfw: bool
    # presences: list[] #TODO: Write presences impl
    voice_states: list[VoiceStateObject] = Field(default_factory=list)
    members: list[GuildMemberObject] = Field(default_factory=list)
    widget_channel_id: ChannelID = Field(default=None)
    discovery_splash: str = Field(default=None)
    region: str = Field(default=None)
    features: GuildFutures = Field(default_factory=list)
    approximate_member_count: Any = Field(default=None)
    approximate_presence_count: Any = Field(default=None)

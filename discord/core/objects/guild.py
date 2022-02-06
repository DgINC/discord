from dataclasses import dataclass, field
from typing import List
from enum import IntEnum, IntFlag

from .types.snowflake import GuildID, OwnerID, AppID, ChannelID
from .base import BaseObject
from .role import Role
from .emojis import Emoji
from .user import User
from .voice import VoiceState


class VerificationLevel(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class MessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class ExplicitContentFilterLevel(IntEnum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class GuildNSFWLevel(IntEnum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class PremiumTier(IntEnum):
    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class SystemChannelFlags(IntFlag):
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0,
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1,
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2,
    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3


class MFALevel(IntEnum):
    NONE = 0
    ELEVATED = 1


GuildFutures = [
    'ANIMATED_ICON',
    'BANNER',
    'COMMERCE',
    'COMMUNITY',
    'DISCOVERABLE',
    'FEATURABLE',
    'INVITE_SPLASH',
    'MEMBER_VERIFICATION_GATE_ENABLED',
    'MONETIZATION_ENABLED',
    'MORE_STICKERS',
    'NEWS',
    'PARTNERED',
    'PREVIEW_ENABLED',
    'PRIVATE_THREADS',
    'ROLE_ICONS',
    'SEVEN_DAY_THREAD_ARCHIVE',
    'THREE_DAY_THREAD_ARCHIVE',
    'TICKETED_EVENTS_ENABLED',
    'VANITY_URL',
    'VERIFIED',
    'VIP_REGIONS',
    'WELCOME_SCREEN_ENABLED'
]


@dataclass
class GuildMember(BaseObject):
    user: User
    nick: str
    avatar: str
    roles: List[Role.id]
    joined_at: int
    premium_since: int
    deaf: bool
    mute: bool
    pending: bool
    permissions: str
    communication_disabled_until: int


@dataclass
class Guild(BaseObject):
    id: GuildID
    name: str
    icon: str
    icon_hash: str
    splash: str
    description: str
    emojis: List[Emoji]
    banner: str
    owner: bool
    owner_id: OwnerID
    application_id: AppID
    afk_channel_id: ChannelID
    afk_timeout: int
    system_channel_id: ChannelID
    widget_enabled: bool
    verification_level: VerificationLevel
    roles: List[Role]
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
    voice_states: List[VoiceState] = field(default_factory=List)
    members: List[GuildMember] = field(default_factory=List)
    channels: 
    widget_channel_id: ChannelID = field(default=None)
    discovery_splash: str = field(default=None)
    region: str = field(default=None)
    features: GuildFutures = field(default_factory=List)

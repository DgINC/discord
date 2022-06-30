from dataclasses import dataclass, field
from enum import IntEnum, IntFlag
from typing import TypeVar

from .applicationobject import ApplicationID
from .base import BaseObject
from .channel import ChannelID, Channel
from .emojis import Emoji
from .role import Role, RoleID
from .stickerobjects import StickerObject
from .types.snowflake import SnowFlake
from .user import User
from .user import UserID
from .voice import VoiceState

GuildID = TypeVar('GuildID', bound=SnowFlake)


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
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
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
class GuildPreviewObject(BaseObject):
    id: GuildID
    name: str
    icon: str
    splash: str
    discovery_splash: str
    emojis: list[Emoji]
    features: list[GuildFutures]
    approximate_member_count: int
    approximate_presence_count: int
    description: str
    stickers: list[StickerObject]


@dataclass
class GuildMemberObject(BaseObject):
    user: User
    nick: str
    avatar: str
    roles: list[RoleID]
    joined_at: int
    premium_since: int
    deaf: bool
    mute: bool
    pending: bool
    permissions: str
    communication_disabled_until: int


@dataclass
class GuildObject(BaseObject):
    id: GuildID
    name: str
    icon: str
    icon_hash: str
    splash: str
    description: str
    emojis: list[Emoji]
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
    roles: list[Role]
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
    channels: list[Channel]
    threads: list[Channel]
    nsfw: bool
    # presences: list[] #TODO: Write presence impl
    voice_states: list[VoiceState] = field(default_factory=list)
    members: list[GuildMemberObject] = field(default_factory=list)
    widget_channel_id: ChannelID = field(default=None)
    discovery_splash: str = field(default=None)
    region: str = field(default=None)
    features: GuildFutures = field(default_factory=list)

from enum import IntFlag, IntEnum
from typing import Final, final

from discord.core.objects.guild.guildmemberobject import GuildMemberObject
from discord.core.objects.guild.guildobject import GuildObject
from discord.core.objects.guild.guildpreviewobject import GuildPreviewObject

__all__ = [
    "VerificationLevel",
    "MessageNotificationLevel",
    "ExplicitContentFilterLevel",
    "GuildNSFWLevel",
    "PremiumTier",
    "SystemChannelFlags",
    "MFALevel",
    "GuildFutures",
    "GuildPreviewObject",
    "GuildMemberObject",
    "GuildObject"
]


@final
class VerificationLevel(IntEnum):
    """
    VerificationLevel
    """
    NONE: Final = 0
    LOW: Final = 1
    MEDIUM: Final = 2
    HIGH: Final = 3
    VERY_HIGH: Final = 4


@final
class MessageNotificationLevel(IntEnum):
    """
    MessageNotificationLevel
    """
    ALL_MESSAGES: Final = 0
    ONLY_MENTIONS: Final = 1


@final
class ExplicitContentFilterLevel(IntEnum):
    """
    ExplicitContentFilterLevel
    """
    DISABLED: Final = 0
    MEMBERS_WITHOUT_ROLES: Final = 1
    ALL_MEMBERS: Final = 2


@final
class GuildNSFWLevel(IntEnum):
    """
    GuildNSFWLevel
    """
    DEFAULT: Final = 0
    EXPLICIT: Final = 1
    SAFE: Final = 2
    AGE_RESTRICTED: Final = 3


@final
class PremiumTier(IntEnum):
    """
    PremiumTier
    """
    NONE: Final = 0
    TIER_1: Final = 1
    TIER_2: Final = 2
    TIER_3: Final = 3


@final
class SystemChannelFlags(IntFlag):
    """
    SystemChannelFlags
    """
    SUPPRESS_JOIN_NOTIFICATIONS: Final = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS: Final = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS: Final = 1 << 2
    SUPPRESS_JOIN_NOTIFICATION_REPLIES: Final = 1 << 3


@final
class MFALevel(IntEnum):
    """
    MFALevel
    """
    NONE: Final = 0
    ELEVATED: Final = 1


GuildFutures: Final = [
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

from enum import IntEnum, IntFlag
from typing import final, Final, NewType

__all__ = [
    "EmbedType",
    "EmbedThumbnailObject",
    "EmbedImageObject",
    "EmbedVideoObject",
    "AutoArchiveDuration",
    "ChannelType",
    "MessageType",
    "VideoQualityMode",
    "MessageFlags",
    "AttachmentObject",
    "ChannelObject",
    "ChannelMention",
    "EmbedObject",
    "EmbedAuthorObject",
    "EmbedFieldObject",
    "EmbedFooterObject",
    "EmbedProviderObject",
    "EmbedStructureObject",
    "MessageObject",
    "MessageActivity",
    "MessageReferenceObject",
    "OverwriteObject",
    "ReactionObject",
    "ThreadMemberObject",
    "ThreadMetadataObject"
]

from core.objects.channel.attachment import AttachmentObject
from core.objects.channel.channel import ChannelObject
from core.objects.channel.channelmention import ChannelMention
from core.objects.channel.embed import EmbedObject
from core.objects.channel.embedstructure import EmbedStructureObject
from core.objects.channel.embedauthor import EmbedAuthorObject
from core.objects.channel.embedfieldobject import EmbedFieldObject
from core.objects.channel.embedfooterobject import EmbedFooterObject
from core.objects.channel.embedproviderobject import EmbedProviderObject
from core.objects.channel.message import MessageObject
from core.objects.channel.messagereference import MessageReferenceObject
from core.objects.channel.overwrite import OverwriteObject
from core.objects.channel.reaction import ReactionObject
from core.objects.channel.threadmemberobject import ThreadMemberObject
from core.objects.channel.threadmetadataobject import ThreadMetadataObject

EmbedType: Final = {'rich', 'image', 'video', 'gifv', 'article', 'link'}

EmbedThumbnailObject = NewType('EmbedThumbnail', EmbedStructureObject)
EmbedImageObject = NewType('EmbedImage', EmbedStructureObject)
EmbedVideoObject = NewType('EmbedVideo', EmbedStructureObject)


@final
class AutoArchiveDuration(IntEnum):
    """
    AutoArchiveDuration
    """
    HOUR: Final = 60
    DAY: Final = 1440
    THREE_DAYS: Final = 4320
    WEEK: Final = 10080


@final
class ChannelType(IntEnum):
    """
    ChannelType
    """
    GUILD_TEXT: Final = 0
    DM: Final = 1
    GUILD_VOICE: Final = 2
    GROUP_DM: Final = 3
    GUILD_CATEGORY: Final = 4
    GUILD_NEWS: Final = 5
    GUILD_STORE: Final = 6
    GUILD_NEWS_THREAD: Final = 10
    GUILD_PUBLIC_THREAD: Final = 11
    GUILD_PRIVATE_THREAD: Final = 12
    GUILD_STAGE_VOICE: Final = 13


@final
class MessageType(IntEnum):
    """
    MessageType
    """
    DEFAULT: Final = 0
    RECIPIENT_ADD: Final = 1
    RECIPIENT_REMOVE: Final = 2
    CALL: Final = 3
    CHANNEL_NAME_CHANGE: Final = 4
    CHANNEL_ICON_CHANGE: Final = 5
    CHANNEL_PINNED_MESSAGE: Final = 6
    GUILD_MEMBER_JOIN: Final = 7
    USER_PREMIUM_GUILD_SUBSCRIPTION: Final = 8
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_1: Final = 9
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_2: Final = 10
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_3: Final = 11
    CHANNEL_FOLLOW_ADD: Final = 12
    GUILD_DISCOVERY_DISQUALIFIED: Final = 14
    GUILD_DISCOVERY_REQUALIFIED: Final = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING: Final = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING: Final = 17
    THREAD_CREATED: Final = 18
    REPLY: Final = 19
    CHAT_INPUT_COMMAND: Final = 20
    THREAD_STARTER_MESSAGE: Final = 21
    GUILD_INVITE_REMINDER: Final = 22
    CONTEXT_MENU_COMMAND: Final = 23


@final
class MessageActivity(IntEnum):
    """
    MessageActivity
    """
    JOIN: Final = 1
    SPECTATE: Final = 2
    LISTEN: Final = 3
    JOIN_REQUEST: Final = 5


@final
class VideoQualityMode(IntEnum):
    """
    VideoQualityMode
    """
    AUTO: Final = 1
    FULL: Final = 2


@final
class MessageFlags(IntFlag):
    """
    MessageFlags
    """
    CROSSPOSTED: Final = 1 << 0
    IS_CROSSPOST: Final = 1 << 1
    SUPPRESS_EMBEDS: Final = 1 << 2
    SOURCE_MESSAGE_DELETED: Final = 1 << 3
    URGENT: Final = 1 << 4
    HAS_THREAD: Final = 1 << 5
    EPHEMERAL: Final = 1 << 6
    LOADING: Final = 1 << 7
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD: Final = 1 << 8

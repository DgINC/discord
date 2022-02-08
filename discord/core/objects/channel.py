from dataclasses import dataclass, field
from enum import IntEnum, IntFlag
from typing import TypeVar, Union, Optional, Annotated, NewType, final

from .emojis import Emoji
from .interactions import MessageInteraction, MessageComponent
from .role import Role
from .sticker import Sticker, StickerItem
from .types.snowflake import SnowFlake
from .base import BaseObject
from .guild import GuildID, GuildMember
from .user import UserID, User
from .application import ApplicationID, Application
from .voice import VoiceRegion
from ..utils.base import MaxLen

ChannelID = TypeVar('ChannelID', bound=SnowFlake)
CategoryID = TypeVar('CategoryID', bound=SnowFlake)
MessageID = TypeVar('MessageID', bound=SnowFlake)
ThreadID = TypeVar('ThreadID', bound=SnowFlake)
AttachID = TypeVar('AttachID', bound=SnowFlake)

EmbedType = {'rich', 'image', 'video', 'gifv', 'article', 'link'}


@final
class AutoArchiveDuration(IntEnum):
    HOUR = 60
    DAY = 1440
    THREE_DAYS = 4320
    WEEK = 10080


@final
class ChannelType(IntEnum):
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_STORE = 6
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13


@final
class MessageType(IntEnum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    GUILD_MEMBER_JOIN = 7
    USER_PREMIUM_GUILD_SUBSCRIPTION = 8
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_1 = 9
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_2 = 10
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23


@final
class MessageActivity(IntEnum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


@final
class VideoQualityMode(IntEnum):
    AUTO = 1
    FULL = 2


@final
class MessageFlags(IntFlag):
    CROSSPOSTED = 1 << 0
    IS_CROSSPOST = 1 << 1
    SUPPRESS_EMBEDS = 1 << 2
    SOURCE_MESSAGE_DELETED = 1 << 3
    URGENT = 1 << 4
    HAS_THREAD = 1 << 5
    EPHEMERAL = 1 << 6
    LOADING = 1 << 7
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8


@dataclass
class Overwrite(BaseObject):
    id: UserID
    type: int
    allow: str
    deny: str


@dataclass
class ThreadMetadata(BaseObject):
    archived: bool
    auto_archive_duration: int


@dataclass
class ThreadMember(BaseObject):
    id: ThreadID
    user_id: UserID
    join_timestamp: int
    flags: int


@dataclass
class ChannelMention(BaseObject):
    id: ChannelID
    guild_id: GuildID
    type: ChannelType
    name: str


@dataclass
class EmbedFooter(BaseObject):
    text: str
    icon_url: str
    proxy_icon_url: str


@dataclass
class Embed(BaseObject):
    url: str
    proxy_url: str
    height: int
    width: int


EmbedThumbnail = NewType('EmbedThumbnail', Embed)
EmbedImage = NewType('EmbedImage', Embed)
EmbedVideo = NewType('EmbedVideo', Embed)


@dataclass
class EmbedProvider(BaseObject):
    name: str
    url: str


@dataclass
class EmbedAuthor(BaseObject):
    name: str
    url: str
    icon_url: str
    proxy_icon_url: str


@dataclass
class EmbedField(BaseObject):
    name: str
    value: str
    inline: bool


@dataclass
class Attachment(BaseObject):
    id: AttachID
    filename: str
    description: str
    content_type: str   # TODO: Generate MIME-type automatically
    size: int
    url: str
    proxy_url: str
    height: int
    width: int
    ephemeral: bool


@dataclass
class Embed(BaseObject):
    title: str
    type: EmbedType
    description: str
    url: str
    timestamp: int
    color: int
    footer: EmbedFooter
    image: EmbedImage
    thumbnail: EmbedThumbnail
    video: EmbedVideo
    provider: EmbedProvider
    author: EmbedAuthor
    fields: list[EmbedField] = field(default_factory=list)


@dataclass
class Reaction(BaseObject):
    count: int
    me: bool
    emoji: Emoji


@dataclass
class MessageActivity(BaseObject):
    type: MessageType
    party_id: str


@dataclass
class MessageReference(BaseObject):
    message_id: MessageID
    channel_id: ChannelID
    guild_id: GuildID
    fail_if_not_exists: bool


@dataclass
class Channel(BaseObject):
    id: ChannelID
    type: ChannelType
    guild_id: GuildID
    position: int
    name: str
    topic: str
    nsfw: bool
    last_message_id: MessageID
    bitrate: int
    user_limit: int
    rate_limit_per_user: int
    recipients: list[User]
    icon: str
    owner_id: UserID
    application_id: ApplicationID
    parent_id: Optional[Union[CategoryID, ChannelID]]
    last_pin_timestamp: Optional[Union[int, None]]
    rtc_region: Optional[Union[VoiceRegion.id, None]]
    video_quality_mode: VideoQualityMode
    message_count: Annotated[int, MaxLen(50)]
    member_count: Annotated[int, MaxLen(50)]
    thread_metadata: ThreadMetadata
    member: ThreadMember
    default_auto_archive_duration: AutoArchiveDuration
    permissions: str
    permission_overwrites: list[Overwrite] = field(default_factory=list)


@dataclass
class Message(BaseObject):
    id: MessageID
    channel_id: ChannelID
    guild_id: GuildID
    author: User
    member: GuildMember
    content: str
    timestamp: int
    edited_timestamp: Optional[Union[int, None]]
    tts: bool
    mention_everyone: bool
    mentions: list[User]    # array of user objects, with an additional partial member field
    mention_roles: list[Role.id]
    mention_channels: list[ChannelMention]
    attachments: list[Attachment]
    embeds: list[Embed]
    reactions: list[Reaction]
    nonce: Optional[Union[int, str]]
    pinned: bool
    webhook_id: SnowFlake   # TODO: Rewrite to Webhook().id
    type: MessageType
    activity: MessageActivity
    application: Application
    application_id: ApplicationID
    message_reference: MessageReference
    flags: MessageFlags
    referenced_message: Optional[Message] = field(hash=False, compare=False, repr=False)
    interaction: MessageInteraction
    thread: Channel
    components: list[MessageComponent]
    sticker_items: list[StickerItem]
    stickers: list[Sticker]

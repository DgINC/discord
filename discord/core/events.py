from enum import IntFlag
from typing import TypeVar, final, Final

from pydantic.dataclasses import dataclass

T = TypeVar('T')

GUILDIntents = [
    "GUILD_CREATE",
    "GUILD_UPDATE",
    "GUILD_DELETE",
    "GUILD_ROLE_CREATE",
    "GUILD_ROLE_UPDATE",
    "GUILD_ROLE_DELETE",
    "CHANNEL_CREATE",
    "CHANNEL_UPDATE",
    "CHANNEL_DELETE",
    "CHANNEL_PINS_UPDATE",
    "THREAD_CREATE",
    "THREAD_UPDATE",
    "THREAD_DELETE",
    "THREAD_LIST_SYNC",
    "THREAD_MEMBER_UPDATE",
    "THREAD_MEMBERS_UPDATE",
    "STAGE_INSTANCE_CREATE",
    "STAGE_INSTANCE_UPDATE",
    "STAGE_INSTANCE_DELETE"
]


@final
class Intents(IntFlag):
    """
    Intents
    """
    GUILDS: Final = 1 << 0
    GUILD_MEMBERS: Final = 1 << 1
    GUILD_BANS: Final = 1 << 2
    GUILD_EMOJIS_AND_STICKERS: Final = 1 << 3
    GUILD_INTEGRATIONS: Final = 1 << 4
    GUILD_WEBHOOKS: Final = 1 << 5
    GUILD_INVITES: Final = 1 << 6
    GUILD_VOICE_STATES: Final = 1 << 7
    GUILD_PRESENCES: Final = 1 << 8
    GUILD_MESSAGES: Final = 1 << 9
    GUILD_MESSAGE_REACTIONS: Final = 1 << 10
    GUILD_MESSAGE_TYPING: Final = 1 << 11
    DIRECT_MESSAGES: Final = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING: Final = 1 << 14
    GUILD_SCHEDULED_EVENTS: Final = 1 << 16


@dataclass
class DispatchObj:
    """
    DispatchObj
    """
    op: int
    d: T
    s: int
    t: str

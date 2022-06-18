from dataclasses import dataclass, field
from enum import IntEnum
from typing import Annotated, Optional, Union

from .emojis import Emoji
from .guildobjects import GuildMemberObject
from .types.snowflake import SnowFlake
from .base import BaseObject
from .user import User
from ..utils.base import MaxLen


class InteractionType(IntEnum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4


@dataclass
class MessageInteraction(BaseObject):
    id: SnowFlake   # TODO: Rewrite to InteractionID
    type: InteractionType
    name: str
    user: User
    member: GuildMemberObject


class ComponentType(IntEnum):
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3


class ButtonStyle(IntEnum):
    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5


@dataclass
class SelectOption(BaseObject):
    label: str
    value: str
    description: str
    emoji: Emoji
    default: bool


@dataclass
class MessageComponent(BaseObject):
    type: ComponentType
    custom_id: Annotated[str, MaxLen(100)]
    disabled: bool
    style: ButtonStyle
    label: str
    emoji: Emoji
    url: str
    options: list[SelectOption]
    placeholder: str
    min_values: int = field(default=1)  # TODO: the minimum number of items that must be chosen; default 1, min 0, max 25
    max_values: int = field(default=1)  # TODO: the maximum number of items that can be chosen; default 1, max 25
    components: list[MessageComponent] = field(default_factory=list)    # TODO: Fix this shit

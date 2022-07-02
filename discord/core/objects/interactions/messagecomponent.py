from __future__ import annotations
from dataclasses import dataclass, field
from typing import Annotated, Any
from typing import TYPE_CHECKING

from discord.core.utils import MaxLen
from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.emojis import EmojiObject
    from discord.core.objects.interactions import ComponentType, ButtonStyle, SelectOptionObject


@dataclass
class MessageComponentObject(BaseObject):
    """
    MessageComponentObject
    """
    type: ComponentType
    custom_id: Annotated[str, MaxLen(100)]
    disabled: bool
    style: ButtonStyle
    label: str
    emoji: EmojiObject
    url: str
    options: list[SelectOptionObject]
    placeholder: str
    min_values: int = field(
        default=1)  # TODO: the minimum number of items that must be chosen; default 1, min 0, max 25
    max_values: int = field(default=1)  # TODO: the maximum number of items that can be chosen; default 1, max 25
    components: list[Any] = field(default_factory=list)  # TODO: Set type to "MessageComponent"

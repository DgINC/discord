from dataclasses import dataclass, field
from typing import Annotated, Any

from core.objects import BaseObject
from core.objects.emojis import EmojiObject
from core.objects.interactions import ComponentType, ButtonStyle
from core.objects.interactions.selectoption import SelectOptionObject
from core.utils.base import MaxLen


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

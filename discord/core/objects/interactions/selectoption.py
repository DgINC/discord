from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.emojis import EmojiObject


@dataclass
class SelectOptionObject(BaseObject):
    """
    SelectOptionObject
    """
    label: str
    value: str
    description: str
    emoji: EmojiObject
    default: bool

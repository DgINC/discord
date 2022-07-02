from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.emojis import EmojiObject


@dataclass
class ReactionObject(BaseObject):
    """
    ReactionObject
    """
    count: int
    me: bool
    emoji: EmojiObject

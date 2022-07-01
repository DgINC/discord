from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class ReactionObject(BaseObject):
    """
    ReactionObject
    """
    count: int
    me: bool
    emoji: Emoji

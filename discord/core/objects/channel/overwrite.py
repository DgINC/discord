from dataclasses import dataclass

from core.objects.types import UserID
from discord.core.objects import BaseObject


@dataclass
class OverwriteObject(BaseObject):
    """
    Overwrite
    """
    id: UserID
    type: int
    allow: str
    deny: str

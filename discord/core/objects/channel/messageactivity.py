from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.channel import MessageType


@dataclass
class MessageActivityObject(BaseObject):
    """
    MessageActivityObject
    """
    type: MessageType
    party_id: str

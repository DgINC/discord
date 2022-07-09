from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

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

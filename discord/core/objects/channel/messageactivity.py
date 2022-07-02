from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.channel import MessageType


@dataclass
class MessageActivityObject(BaseObject):
    """
    MessageActivityObject
    """
    type: MessageType
    party_id: str

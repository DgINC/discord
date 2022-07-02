from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.guild import GuildMemberObject
from core.objects.interactions import InteractionType
from core.objects.types import SnowFlake
from core.objects.user import UserObject


@dataclass
class MessageInteractionObject(BaseObject):
    """
    MessageInteractionObject
    """
    id: SnowFlake  # TODO: Rewrite to InteractionID
    type: InteractionType
    name: str
    user: UserObject
    member: GuildMemberObject

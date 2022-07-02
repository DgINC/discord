from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.types import BotID, IntegrID


@dataclass
class RoleTagsObject(BaseObject):
    """
    RoleTagsObject
    """
    bot_it: BotID
    integration_id: IntegrID
    premium_subscriber: None

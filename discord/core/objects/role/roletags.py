from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import BotID, IntegrID


@dataclass
class RoleTagsObject(BaseObject):
    """
    RoleTagsObject
    """
    bot_it: BotID
    integration_id: IntegrID
    premium_subscriber: None

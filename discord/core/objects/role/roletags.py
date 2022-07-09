from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

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

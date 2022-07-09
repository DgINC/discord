from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.guild import GuildMemberObject
    from discord.core.objects.interactions import InteractionType
    from discord.core.objects.types import SnowFlake
    from discord.core.objects.user import UserObject


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

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.types import ThreadID, UserID


@dataclass
class ThreadMemberObject(BaseObject):
    """
    ThreadMember
    """
    id: ThreadID
    user_id: UserID
    join_timestamp: int
    flags: int

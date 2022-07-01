from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.types import ThreadID, UserID


@dataclass
class ThreadMember(BaseObject):
    """
    ThreadMember
    """
    id: ThreadID
    user_id: UserID
    join_timestamp: int
    flags: int

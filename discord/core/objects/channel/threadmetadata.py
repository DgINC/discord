from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class ThreadMetadata(BaseObject):
    """
    ThreadMetadata
    """
    archived: bool
    auto_archive_duration: int

from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class ThreadMetadataObject(BaseObject):
    """
    ThreadMetadata
    """
    archived: bool
    auto_archive_duration: int

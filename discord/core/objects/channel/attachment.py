from dataclasses import dataclass

from core.objects import BaseObject
from core.objects.types import AttachID


@dataclass
class AttachmentObject(BaseObject):
    """
    AttachmentObject
    """
    id: AttachID
    filename: str
    description: str
    content_type: str  # TODO: Generate MIME-type automatically
    size: int
    url: str
    proxy_url: str
    height: int
    width: int
    ephemeral: bool

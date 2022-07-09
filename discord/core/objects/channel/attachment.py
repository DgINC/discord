from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

if TYPE_CHECKING:
    from discord.core.objects import BaseObject
    from discord.core.objects.types import AttachID


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

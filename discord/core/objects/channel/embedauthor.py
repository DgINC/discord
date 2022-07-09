from __future__ import annotations

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject


@dataclass
class EmbedAuthorObject(BaseObject):
    """
    EmbedAuthor
    """
    name: str
    url: str
    icon_url: str
    proxy_icon_url: str

from __future__ import annotations
from dataclasses import dataclass

from discord.core.objects import BaseObject


@dataclass
class EmbedFooterObject(BaseObject):
    """
    EmbedFooter
    """
    text: str
    icon_url: str
    proxy_icon_url: str

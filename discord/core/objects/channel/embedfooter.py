from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedFooter(BaseObject):
    """
    EmbedFooter
    """
    text: str
    icon_url: str
    proxy_icon_url: str

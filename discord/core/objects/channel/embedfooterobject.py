from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedFooterObject(BaseObject):
    """
    EmbedFooter
    """
    text: str
    icon_url: str
    proxy_icon_url: str

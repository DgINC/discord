from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedAuthor(BaseObject):
    """
    EmbedAuthor
    """
    name: str
    url: str
    icon_url: str
    proxy_icon_url: str

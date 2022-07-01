from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedProvider(BaseObject):
    """
    EmbedProvider
    """
    name: str
    url: str

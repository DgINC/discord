from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedProviderObject(BaseObject):
    """
    EmbedProvider
    """
    name: str
    url: str

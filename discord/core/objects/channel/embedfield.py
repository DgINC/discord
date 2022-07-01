from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedField(BaseObject):
    """
    EmbedField
    """
    name: str
    value: str
    inline: bool

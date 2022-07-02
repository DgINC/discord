from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class EmbedFieldObject(BaseObject):
    """
    EmbedField
    """
    name: str
    value: str
    inline: bool

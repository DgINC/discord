from dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class VoiceRegionObject(BaseObject):
    """
    VoiceRegionObject
    """
    id: str
    name: str
    optional: bool
    deprecated: bool
    custom: bool

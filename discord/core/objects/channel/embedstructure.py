from dataclasses import dataclass, field

from core.objects import BaseObject


@dataclass
class EmbedStructureObject(BaseObject):    # TODO: Find out the correct name of the object
    """
    Embed
    """
    url: str
    proxy_url: str
    height: int
    width: int

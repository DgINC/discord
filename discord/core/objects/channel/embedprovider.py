from __future__ import annotations
from dataclasses import dataclass

from discord.core.objects import BaseObject


@dataclass
class EmbedProviderObject(BaseObject):
    """
    EmbedProvider
    """
    name: str
    url: str

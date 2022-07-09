from __future__ import annotations

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject


@dataclass
class EmbedProviderObject(BaseObject):
    """
    EmbedProvider
    """
    name: str
    url: str

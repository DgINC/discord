from enum import IntFlag
from typing import final, Final
from discord.core.objects.application.applicationobject import ApplicationObject

__all__ = [
    "ApplicationFlag",
    "ApplicationObject"
]


@final
class ApplicationFlag(IntFlag):
    """
    ApplicationFlag
    """
    GATEWAY_PRESENCE: Final = 1 << 12
    GATEWAY_PRESENCE_LIMITED: Final = 1 << 13
    GATEWAY_GUILD_MEMBERS: Final = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED: Final = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT: Final = 1 << 16
    EMBEDDED: Final = 1 << 17
    GATEWAY_MESSAGE_CONTENT: Final = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED: Final = 1 << 19
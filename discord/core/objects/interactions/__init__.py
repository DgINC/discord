from enum import IntEnum
from typing import final, Final

__all__ = [
    "InteractionType",
    "ComponentType",
    "ButtonStyle",
    "MessageComponentObject",
    "MessageInteractionObject",
    "SelectOptionObject"
]

from core.objects.interactions.messagecomponent import MessageComponentObject
from core.objects.interactions.messageinteraction import MessageInteractionObject
from core.objects.interactions.selectoption import SelectOptionObject


@final
class InteractionType(IntEnum):
    """
    InteractionType
    """
    PING: Final = 1
    APPLICATION_COMMAND: Final = 2
    MESSAGE_COMPONENT: Final = 3
    APPLICATION_COMMAND_AUTOCOMPLETE: Final = 4


@final
class ComponentType(IntEnum):
    """
    ComponentType
    """
    ACTION_ROW: Final = 1
    BUTTON: Final = 2
    SELECT_MENU: Final = 3


@final
class ButtonStyle(IntEnum):
    """
    ButtonStyle
    """
    PRIMARY: Final = 1
    SECONDARY: Final = 2
    SUCCESS: Final = 3
    DANGER: Final = 4
    LINK: Final = 5

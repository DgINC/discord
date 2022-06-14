from enum import Enum
from typing import Final


class MaxLen:
    def __init__(self, value):
        self.value = value


class METH(str, Enum):
    POST: Final[str] = "POST"
    PUT: Final[str] = "PUT"
    GET: Final[str] = "GET"
    PATCH: Final[str] = "PATCH"
    DELETE: Final[str] = "DELETE"
    OPTIONS: Final[str] = "OPTIONS"
    HEAD: Final[str] = "HEAD"

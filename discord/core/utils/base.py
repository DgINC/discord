from types import Final
from typing import Enum

class METH(str, Enum):
    PUT: Final[str] = "PUT"
    GET: Final[str] = "GET"
    PATCH: Final[str] = "PATCH"
    DELETE: Final[str] = "DELETE"
    OPTIONS: Final[str] = "OPTIONS"
    HEAD: Final[str] = "HEAD"

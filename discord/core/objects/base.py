from logging import warn
from typing import Any, Tuple

from orjson import orjson
from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder


class DeprecatedMetaclass(type):

    def __getattribute__(self, item) -> Any:
        if item == "deprecated":
            warn(f'{item} class variable is deprecated', DeprecationWarning)
            return type.__getattribute__(self, item)
        return super(DeprecatedMetaclass, self).__getattribute__(item)


class MyConfig:
    validate_assignment = False
    require_by_default = False


class MetaObject(type):
    def __new__(mcs, name: str, bases: Tuple[type, ...], dictionary: dict[str, Any], **kwargs: Any):
        return super(MetaObject, mcs).__new__(mcs, name, bases, dictionary)

    def __init__(cls, name: str, bases: Tuple[type, ...], dictionary: dict[str, Any], **kwargs: Any):
        super(MetaObject, cls).__init__(name, bases, dictionary)


@dataclass(config=MyConfig)
class BaseObject(object, metaclass=MetaObject):
    def to_json(self) -> str:
        # orjson.dumps returns bytes, to match standard json.dumps we need to decode
        return orjson.dumps(self, default=pydantic_encoder).decode()
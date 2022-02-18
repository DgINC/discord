import dataclasses
from typing import List, Any, Tuple

import orjson
from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder


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


@dataclass(config=MyConfig)
class Error(BaseObject):
    code: int
    message: str
    sty: int = dataclasses.field(default=None, metadata={"deprecated": True})


@dataclass(config=MyConfig)
class BaseJsonObject(BaseObject):
    code: int
    message: str
    errors: List[Error]


json_data = '{"code":50035,' \
            '"message":"Invalid Form Body",' \
            '"errors":[{"code":"123","message":"Command exceeds maximum size (4000)"},' \
            '{"code":"321","message":"Command exceeds maximum size (4001)", "sty": 4001}]}'

dct: dict = orjson.loads(json_data)

result = BaseJsonObject(**dct)
#print(result)

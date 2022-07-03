import orjson

from dataclasses import field
from typing import List
from pydantic.dataclasses import dataclass

from core.objects import BaseObject


@dataclass
class Error(BaseObject):
    """
    Error
    """
    code: int
    message: str
    sty: int = field(default=None, metadata={"deprecated": True})


@dataclass
class BaseJsonObject(BaseObject):
    """
    BaseJsonObject
    """
    code: int
    message: str
    errors: List[Error]


json_data = '{"code":50035,' \
            '"message":"Invalid Form Body",' \
            '"errors":[{"code":"123","message":"Command exceeds maximum size (4000)"},' \
            '{"code":"321","message":"Command exceeds maximum size (4001)", "sty": 4001}]}'

json_data2 = '{"code":50035,' \
            '"message":"Invalid Form Body",' \
            '"errors":[{"code":"123","message":"Command exceeds maximum size (4000)"},' \
            '{"code":"321","message":"Command exceeds maximum size (4001)", "sty": 4001}]}'

dct: dict = orjson.loads(json_data)

result = BaseJsonObject(**dct)
print(result)

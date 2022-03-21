from dataclasses import dataclass, fields
from warnings import warn
from typing import Any
from .types.snowflake import SnowFlake

from pydantic import BaseModel


class DeprecatedMetaclass(type):

    def __getattribute__(self, item) -> Any:
        if item == "deprecated":
            warn(f'{item} class variable is deprecated', DeprecationWarning)
            return type.__getattribute__(self, item)
        return super(DeprecatedMetaclass, self).__getattribute__(item)


@dataclass
class BaseObject(BaseModel):
    __metaclass__ = DeprecatedMetaclass

    class Config:
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


@dataclass
class RequestMixin:
    @classmethod
    def from_request(cls, request):
        values = request.get("input")
        return cls(**values)

    def to_json(self):
        return json.dumps(asdict(self))

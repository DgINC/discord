from __future__ import annotations

import logging
import re
from dataclasses import field, fields

import orjson
from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject

log = logging.getLogger("Errors")


@dataclass
class Error(BaseObject):
    """
    Error
    """
    code: str
    message: str


@dataclass
class Errors(BaseObject):  # re.sub('"[_]+', '"', json_data2)
    """
    Errors
    """
    errors: list[Error]


@dataclass
class RequestErrorObject(BaseObject):
    """
    BaseJsonObject
    """
    code: int = None
    errors: Errors = None
    message: str = field(default=None, metadata={"deprecated": True})


json_data2 = '{"code":50035, "message":"Invalid Form Body", "errors": {"_errors":[{' \
             '"code":"APPLICATION_COMMAND_TOO_LARGE", "message":"Command exceeds maximum size (4000)"}]}} '

strin = re.sub('"[_]+', '"', json_data2)

dct = orjson.loads(strin)

result = RequestErrorObject(**dct)
for k in fields(result):
    if k.metadata.get("deprecated") and not None:
        log.warning(f'Variable "{k.name}" of {result.__class__.__name__} class is deprecated!')

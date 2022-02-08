import json
from types import SimpleNamespace
from typing import TypeVar
from dataclasses import dataclass, field


@dataclass
class Errors(SimpleNamespace):
    pass


@dataclass
class BaseError:
    code: int
    message: str
    errors: Errors = field()


@dataclass
class ObjectError(BaseError):
    pass


JSON_DATA = '{"code":50035,' \
            '"errors":{' \
                '"access_token":{' \
                    '"_errors":[{' \
                        '"code":"BASE_TYPE_REQUIRED",' \
                        '"message":"This field is required"' \
                    '}]' \
                '}' \
            '},' \
            '"message":"Invalid Form Body"}'

x = json.loads(JSON_DATA, object_hook=lambda d: ObjectError(**d))

print(x)

from dataclasses import dataclass
from warnings import warn
from typing import Any


class DeprecatedMetaclass(type):

    def __getattribute__(self, item) -> Any:
        if item is None:
            warn(f'{item} class variable is deprecated', DeprecationWarning)
            return type.__getattribute__(self, item)
        return super(DeprecatedMetaclass, self).__getattribute__(item)


@dataclass
class BaseObject(object, metaclass=DeprecatedMetaclass):
    pass

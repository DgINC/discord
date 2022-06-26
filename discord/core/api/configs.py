from abc import ABC, abstractmethod
from contextlib import AsyncContextDecorator
from typing import NoReturn


class OAuthConfigInterface(ABC):
    @classmethod
    def __subclasshook__(cls, c):
        if cls is OAuthConfigInterface:
            if any("__iter__" in b.__dict__ for b in c.__mro__):
                return True
        return NotImplemented

    @property
    @abstractmethod
    async def client_id(self) -> int:
        ...

    @client_id.setter
    @abstractmethod
    async def client_id(self, value) -> NoReturn:
        ...

    @client_id.getter
    @abstractmethod
    async def client_id(self) -> int:
        ...

    @client_id.deleter
    @abstractmethod
    async def client_id(self) -> NoReturn:
        ...

    @property
    @abstractmethod
    async def client_secret(self) -> str:
        ...

    @property
    @abstractmethod
    async def credentials(self) -> str:
        ...

    @credentials.getter
    @abstractmethod
    async def credentials(self) -> str:
        ...

    @credentials.setter
    @abstractmethod
    async def credentials(self, value) -> NoReturn:
        ...

    @credentials.deleter
    @abstractmethod
    async def credentials(self) -> NoReturn:
        ...

    @property
    @abstractmethod
    async def redirect_uri(self) -> str:
        ...

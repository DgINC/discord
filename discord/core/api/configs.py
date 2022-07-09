from abc import ABC, abstractmethod
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
    def client_id(self) -> int:
        ...

    @client_id.setter
    @abstractmethod
    def client_id(self, value) -> NoReturn:
        ...

    @client_id.getter
    @abstractmethod
    def client_id(self) -> int:
        ...

    @client_id.deleter
    @abstractmethod
    def client_id(self) -> NoReturn:
        ...

    @property
    @abstractmethod
    def client_secret(self) -> str:
        ...

    @property
    @abstractmethod
    def credentials(self) -> str:
        ...

    @credentials.getter
    @abstractmethod
    def credentials(self) -> str:
        ...

    @credentials.setter
    @abstractmethod
    def credentials(self, value) -> NoReturn:
        ...

    @credentials.deleter
    @abstractmethod
    def credentials(self) -> NoReturn:
        ...

    @property
    @abstractmethod
    def redirect_uri(self) -> str:
        ...

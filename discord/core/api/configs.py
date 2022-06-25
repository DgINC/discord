from abc import ABC, abstractmethod
from typing import NoReturn


class OAuthSessionConfigInterface(ABC):
    """@classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_data') and
                callable(subclass.load_data_source) or
                NotImplemented)

    @property
    @abstractmethod
    async def version(self) -> int:
        raise NotImplementedError

    @version.setter
    @abstractmethod
    async def version(self, value) -> NoReturn:
        raise NotImplementedError

    @version.getter
    @abstractmethod
    async def version(self) -> int:
        raise NotImplementedError"""

    @property
    @abstractmethod
    async def client_id(self) -> int:
        raise NotImplementedError

    @client_id.setter
    @abstractmethod
    async def client_id(self, value) -> NoReturn:
        raise NotImplementedError

    @client_id.getter
    @abstractmethod
    async def client_id(self) -> int:
        raise NotImplementedError

    @client_id.deleter
    @abstractmethod
    async def client_id(self) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    async def client_secret(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    async def credentials(self) -> str:
        raise NotImplementedError

    @credentials.getter
    @abstractmethod
    async def credentials(self) -> str:
        raise NotImplementedError

    @credentials.setter
    @abstractmethod
    async def credentials(self, value) -> NoReturn:
        raise NotImplementedError

    @credentials.deleter
    @abstractmethod
    async def credentials(self) -> NoReturn:
        raise NotImplementedError

    @property
    @abstractmethod
    async def redirect_uri(self) -> str:
        raise NotImplementedError

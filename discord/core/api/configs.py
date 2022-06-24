from abc import ABC, abstractmethod


class SessionConfigInterface(ABC):
    """@classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_data') and
                callable(subclass.load_data_source) or
                NotImplemented)"""

    @abstractmethod
    @property
    async def client_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    @client_id.setter
    async def client_id(self, value):
        raise NotImplementedError

    @abstractmethod
    @client_id.getter
    async def client_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    @client_id.deleter
    async def client_id(self):
        raise NotImplementedError

    @abstractmethod
    @property
    async def client_secret(self) -> str:
        raise NotImplementedError

    @abstractmethod
    @property
    async def redirect_uri(self) -> str:
        raise NotImplementedError

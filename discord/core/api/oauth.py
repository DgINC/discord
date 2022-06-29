from abc import ABC, abstractmethod
from typing import NoReturn, Any


class OAuth2SessionInterface(ABC):

    @classmethod
    def __subclasshook__(cls, c):
        if cls is OAuth2SessionInterface:
            if any("__iter__" in b.__dict__ for b in c.__mro__):
                return True
        return NotImplemented

    @property
    @abstractmethod
    def state(self) -> str:
        ...

    @state.getter
    @abstractmethod
    def state(self) -> str:
        ...

    @state.setter
    @abstractmethod
    def state(self, value: Any) -> NoReturn:
        ...

    @state.deleter
    @abstractmethod
    def state(self) -> NoReturn:
        ...

    @property
    @abstractmethod
    def code_verifier(self) -> str:
        ...

    @code_verifier.getter
    @abstractmethod
    def code_verifier(self) -> str:
        ...

    @code_verifier.setter
    @abstractmethod
    def code_verifier(self, value: Any) -> NoReturn:
        ...

    @code_verifier.deleter
    @abstractmethod
    def code_verifier(self) -> NoReturn:
        ...

    @property
    @abstractmethod
    def code_challenge(self) -> str:
        ...

    @code_challenge.getter
    @abstractmethod
    def code_challenge(self) -> str:
        ...

    @code_challenge.setter
    @abstractmethod
    def code_challenge(self, value: Any) -> NoReturn:
        ...

    @code_challenge.deleter
    @abstractmethod
    def code_challenge(self) -> NoReturn:
        ...

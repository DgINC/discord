import abc


class SessionConfigInterface(metaclass=abc.ABCMeta):
    """@classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_data') and
                callable(subclass.load_data_source) or
                NotImplemented)"""

    @property
    def client_id(self) -> str:
        raise NotImplementedError

    @client_id.setter
    def client_id(self, value) -> str:
        raise NotImplementedError

    @client_id.getter
    def client_id(self) -> str:
        raise NotImplementedError

    @client_id.deleter
    def client_id(self):
        raise NotImplementedError

    @property
    def client_secret(self) -> str:
        raise NotImplementedError

    @property
    def redirect_uri(self) -> str:
        raise NotImplementedError

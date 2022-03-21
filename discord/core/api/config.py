import abc


class ConfigInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_data') and
                callable(subclass.load_data_source) or
                NotImplemented)

    @property
    def version(self) -> str:
        raise NotImplementedError

    @property
    def client_id(self) -> str:
        raise NotImplementedError

    @property
    def client_secret(self) -> str:
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_data(self) -> dict:
    #    raise NotImplementedError

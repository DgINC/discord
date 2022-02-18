from typing import Type, Any, Callable, Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    class Event:
        pass

def dataclass(
    _cls: Optional[Type[Any]] = None,
    *,
    init: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = False,
    unsafe_hash: bool = False,
    frozen: bool = False,
    config: Type[Any] = None,
) -> Union[Callable[[Type[Any]], Type['Dataclass']], Type['Dataclass']]:
    """
    Like the python standard lib dataclasses but with type validation.

    Arguments are the same as for standard dataclasses, except for validate_assignment which has the same meaning
    as Config.validate_assignment.
    """

    def wrap(cls: Type[Any]) -> Type['Dataclass']:
        return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen, config)

    if _cls is None:
        return wrap

    return wrap(_cls)
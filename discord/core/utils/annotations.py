from functools import wraps
from typing import get_type_hints, get_origin, get_args, Annotated

from discord.core.utils import MaxLen


def check_annotations(func):
    """

    :param func:
    :return:
    """

    @wraps(func)
    def wrapped(**kwargs):
        # perform runtime annotation checking
        # first, get type hints from function
        type_hints = get_type_hints(func, include_extras=True)
        for param, hint in type_hints.items():
            # only process annotated types
            if get_origin(hint) is not Annotated:
                continue
            # get base type and additional arguments
            hint_type, *hint_args = get_args(hint)
            # if a list type is detected, process the args
            if hint_type is list or get_origin(hint_type) is list:
                for arg in hint_args:
                    # if MaxLen arg is detected, process it
                    if isinstance(arg, MaxLen):
                        max_len = arg.value
                        actual_len = len(kwargs[param])
                        if actual_len > max_len:
                            raise ValueError(f"Parameter '{param}' cannot have a length "
                                             f"larger than {max_len} (got length {actual_len}).")
        # execute function once all checks passed
        return func(**kwargs)

    return wrapped

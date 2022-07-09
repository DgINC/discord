from dataclasses import asdict, fields
from enum import Enum
from typing import Any, Tuple, final, Union, TYPE_CHECKING, Dict, Set, List, AbstractSet, Mapping, Generator, Sequence, \
    Optional, Callable, no_type_check, cast, NoReturn, ClassVar, Type

from orjson import orjson
from pydantic import BaseConfig, Extra, validate_model
from pydantic.class_validators import AnyCallable
from pydantic.dataclasses import dataclass
from pydantic.fields import FieldInfo, ModelField
from pydantic.typing import is_namedtuple

if TYPE_CHECKING:
    TupleGenerator = Generator[Tuple[str, Any], None, None]
    DictStrAny = Dict[str, Any]
    DictAny = Dict[Any, Any]
    SetStr = Set[str]
    ListStr = List[str]
    IntStr = Union[int, str]
    AbstractSetIntStr = AbstractSet[IntStr]
    DictIntStrAny = Dict[IntStr, Any]
    MappingIntStrAny = Mapping[IntStr, Any]
    CallableGenerator = Generator[AnyCallable, None, None]
    ReprArgs = Sequence[Tuple[Optional[str], Any]]
    AnyClassMethod = classmethod[Any]

__all__ = (
    "BaseObject"
)

from pydantic.utils import ValueItems, sequence_like

_missing = object()
ROOT_KEY = '__root__'


def strip(string: str) -> str:
    return ''.join(word for word in string.lstrip('_'))


@final
class ObjectsConfig(BaseConfig):
    """
    MyConfig
    """
    allow_population_by_field_name = True
    extra = Extra.allow
    # alias_generator = strip
    # validate_assignment = False
    # require_by_default = False
    json_loads = orjson.loads
    json_dumps = orjson.dumps
    # json_encoders = pydantic_encoder


class MetaObject(type):
    """
    MetaObject
    """

    def __new__(mcs, name: str, bases: Tuple[Type, ...], dictionary: Dict[str, Any], **kwargs: Any):
        return super(MetaObject, mcs).__new__(mcs, name, bases, dictionary, **kwargs)

    def __init__(cls, name: str, bases: Tuple[Type, ...], dictionary: Dict[str, Any], **kwargs: Any):
        super(MetaObject, cls).__init__(name, bases, dictionary, **kwargs)

    def __getattribute__(self, item) -> Any:
        return super(MetaObject, self).__getattribute__(item)


@dataclass(config=ObjectsConfig)
class BaseObject:
    """
    :class: BaseObject
    """
    by_alias: ClassVar[bool] = False

    """def __repr_args__(self) -> 'ReprArgs':
        return [
            (k, v) for k, v in self.__dict__.items() if k not in self.__fields__ or self.__fields__[k].field_info.repr
        ]"""

    def __init__(self, **data: Any) -> None:
        """
        Create a new model by parsing and validating input data from keyword arguments.

        Raises ValidationError if the input data cannot be parsed to form a valid model.
        """
        # Uses something other than `self` the first arg to allow "self" as a settable attribute
        values, fields_set, validation_error = validate_model(self.__pydantic_model__, data)
        if validation_error:
            raise validation_error
        try:
            object.__setattr__(self, '__dict__', values)
        except TypeError as e:
            raise TypeError(
                'Model values must be a dict; you may not have returned a dictionary from a root validator'
            ) from e
        object.__setattr__(self, '__fields_set__', fields_set)
        self._init_private_attributes()

    def by_alias(self) -> NoReturn:
        self.by_alias = True

    @classmethod
    @no_type_check
    def _get_value(
            cls,
            v: Any,
            to_dict: bool,
            by_alias: bool,
            include: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']],
            exclude: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']],
            exclude_unset: bool,
            exclude_defaults: bool,
            exclude_none: bool,
    ) -> Any:

        if isinstance(v, BaseObject):
            if to_dict:
                v_dict = v.to_dict(
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    include=include,
                    exclude=exclude,
                    exclude_none=exclude_none,
                )
                if ROOT_KEY in v_dict:
                    return v_dict[ROOT_KEY]
                return v_dict
            else:
                return v.copy(include=include, exclude=exclude)

        value_exclude = ValueItems(v, exclude) if exclude else None
        value_include = ValueItems(v, include) if include else None

        if isinstance(v, dict):
            return {
                k_: cls._get_value(
                    v_,
                    to_dict=to_dict,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    include=value_include and value_include.for_element(k_),
                    exclude=value_exclude and value_exclude.for_element(k_),
                    exclude_none=exclude_none,
                )
                for k_, v_ in v.items()
                if (not value_exclude or not value_exclude.is_excluded(k_))
                   and (not value_include or value_include.is_included(k_))
            }

        elif sequence_like(v):
            seq_args = (
                cls._get_value(
                    v_,
                    to_dict=to_dict,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    include=value_include and value_include.for_element(i),
                    exclude=value_exclude and value_exclude.for_element(i),
                    exclude_none=exclude_none,
                )
                for i, v_ in enumerate(v)
                if (not value_exclude or not value_exclude.is_excluded(i))
                   and (not value_include or value_include.is_included(i))
            )

            return v.__class__(*seq_args) if is_namedtuple(v.__class__) else v.__class__(seq_args)

        elif isinstance(v, Enum) and getattr(cls.__pydantic_model__.Config, 'use_enum_values', False):
            return v.value

        else:
            return v

    def _iter(
            self,
            to_dict: bool = False,
            by_alias: bool = False,
            include: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            exclude: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            skip_defaults: bool = False,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
    ) -> 'TupleGenerator':

        # Merge field set excludes with explicit exclude parameter with explicit overriding field set options.
        # The extra "is not None" guards are not logically necessary but optimizes performance for the simple case.
        if exclude is not None or self.__pydantic_model__.__exclude_fields__ is not None:
            exclude = ValueItems.merge(self.__pydantic_model__.__exclude_fields__, exclude)

        if include is not None or self.__pydantic_model__.__include_fields__ is not None:
            include = ValueItems.merge(self.__pydantic_model__.__include_fields__, include, intersect=True)

        allowed_keys = self._calculate_keys(
            include=include, exclude=exclude, exclude_unset=exclude_unset, skip_defaults=skip_defaults
        )
        if allowed_keys is None and not (to_dict or by_alias or exclude_unset or exclude_defaults or exclude_none):
            # huge boost for plain _iter()
            yield from self.__dict__.items()
            return

        value_exclude = ValueItems(self, exclude) if exclude is not None else None
        value_include = ValueItems(self, include) if include is not None else None

        for field_key, v in self.__dict__.items():
            if (allowed_keys is not None and field_key not in allowed_keys) or (exclude_none and v is None):
                continue

            if exclude_defaults:
                model_field = self.__pydantic_model__.__fields__.get(field_key)
                if not getattr(model_field, 'required', True) and getattr(model_field, 'default', _missing) == v:
                    continue

            if by_alias and field_key in self.__pydantic_model__.__fields__:
                dict_key = self.__pydantic_model__.__fields__[field_key].alias
            else:
                dict_key = field_key

            if to_dict or value_include or value_exclude:
                v = self._get_value(
                    v,
                    to_dict=to_dict,
                    by_alias=by_alias,
                    include=value_include and value_include.for_element(field_key),
                    exclude=value_exclude and value_exclude.for_element(field_key),
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    exclude_none=exclude_none,
                )
            yield dict_key, v

    def _calculate_keys(
            self,
            include: Optional['MappingIntStrAny'],
            exclude: Optional['MappingIntStrAny'],
            skip_defaults: bool,
            exclude_unset: bool,
            update: Optional['DictStrAny'] = None,
    ) -> Optional[AbstractSet[str]]:

        keys: Set[str] = set()
        if skip_defaults:
            for f in fields(self):
                if isinstance(model_field, ModelField):
                    if not (isinstance(f.default, FieldInfo) and hasattr(f.default, 'default')):
                        print(f)
                        keys.add(f.name)

        elif exclude_unset:
            pass

        else:
            for key in asdict(self):
                keys.add(key)

        if include is not None:
            keys.intersection_update(include.keys())

        if update is not None:
            keys.difference_update(update.keys())

        if exclude is not None:
            for k, v in exclude.items():
                if ValueItems.is_true(v):
                    keys.discard(k)
        return keys

    def to_dict(
            self,
            *,
            include: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            exclude: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            by_alias: bool = False,
            skip_defaults: bool = False,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
    ) -> 'DictStrAny':
        """
        Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

        """
        return dict(
            self._iter(
                to_dict=True,
                by_alias=by_alias,
                include=include,
                exclude=exclude,
                skip_defaults=skip_defaults,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
            )
        )

    def to_json(
            self,
            *,
            include: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            exclude: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            by_alias: bool = False,
            skip_defaults: bool = False,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            encoder: Optional[Callable[[Any], Any]] = None,
            models_as_dict: bool = True,
            **dumps_kwargs: Any,
    ) -> str:
        """
        Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

        `encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.
        """
        encoder = cast(Callable[[Any], Any], encoder or self.__pydantic_model__.__json_encoder__)

        # We don't directly call `self.dict()`, which does exactly this with `to_dict=True`
        # because we want to be able to keep raw `BaseModel` instances and not as `dict`.
        # This allows users to write custom JSON encoders for given `BaseModel` classes.
        data = dict(
            self._iter(
                to_dict=models_as_dict,
                by_alias=by_alias,
                include=include,
                exclude=exclude,
                skip_defaults=skip_defaults,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
            )
        )
        if self.__pydantic_model__.__custom_root_type__:
            data = data[ROOT_KEY]

        return self.__pydantic_model__.__config__.json_dumps(data, default=encoder, **dumps_kwargs)

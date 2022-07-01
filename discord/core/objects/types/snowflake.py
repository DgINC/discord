from dataclasses import dataclass, field
from typing import Final, TypeVar, Generic

T = TypeVar('T', int, str)


@dataclass
class SnowFlake(Generic[T]):
    worker_id_bits: Final = field(default=5, init=False)
    process_id_bits: Final = field(default=5, init=False)
    increment: Final = field(default=12, init=False)
    value: T


@dataclass
class SnowFlakeTimestamp(SnowFlake[T]):
    __slots__ = SnowFlake.__slots__

    discord_epoch: Final = field(default=1420070400000, init=False)

    def to_unix_timestamp(self) -> int:
        ret: int

        if isinstance(self.value, str):
            temp: int = int(self.value)
        else:
            temp: int = self.value

        ret = ((temp >> self.worker_id_bits >> self.process_id_bits >> self.increment) + self.discord_epoch)
        return ret

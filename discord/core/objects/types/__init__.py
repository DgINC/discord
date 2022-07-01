from typing import Final, TypeVar
from typing import TypeAlias

from discord.core.objects.types.snowflake import SnowFlake

HttpMethod: TypeAlias = Final[str]

ApplicationID = TypeVar('ApplicationID', bound=SnowFlake)
ChannelID = TypeVar('ChannelID', bound=SnowFlake)
CategoryID = TypeVar('CategoryID', bound=SnowFlake)
MessageID = TypeVar('MessageID', bound=SnowFlake)
ThreadID = TypeVar('ThreadID', bound=SnowFlake)
AttachID = TypeVar('AttachID', bound=SnowFlake)
EmojiID = TypeVar('EmojiID', bound=SnowFlake)
GuildID = TypeVar('GuildID', bound=SnowFlake)
BotID = TypeVar('BotID', bound=SnowFlake)
IntegrID = TypeVar('IntegrID', bound=SnowFlake)
RoleID = TypeVar('RoleID', bound=SnowFlake)
StickerID = TypeVar('StickerID', bound=SnowFlake)
UserID = TypeVar('UserID', bound=SnowFlake)

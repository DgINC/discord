from __future__ import annotations

from dataclasses import field
from typing import Optional, Union, Annotated
from typing import TYPE_CHECKING

from pydantic.dataclasses import dataclass

from discord.core.objects import BaseObject
from discord.core.utils import MaxLen

if TYPE_CHECKING:
    from discord.core.objects.channel import ChannelType, ThreadMetadataObject, ThreadMemberObject, \
        AutoArchiveDuration, OverwriteObject, VideoQualityMode
    from discord.core.objects.types import ChannelID, GuildID, MessageID, UserID, ApplicationID, CategoryID
    from discord.core.objects.user import UserObject
    from discord.core.objects.voice import VoiceRegionObject


@dataclass
class ChannelObject(BaseObject):
    """
    ChannelObject
    """
    id: ChannelID
    type: ChannelType
    guild_id: GuildID
    position: int
    name: str
    topic: str
    nsfw: bool
    last_message_id: MessageID
    bitrate: int
    user_limit: int
    rate_limit_per_user: int
    recipients: list[UserObject]
    icon: str
    owner_id: UserID
    application_id: ApplicationID
    parent_id: Optional[Union[CategoryID, ChannelID]]
    last_pin_timestamp: Optional[int, None]
    rtc_region: Optional[VoiceRegionObject.id]
    video_quality_mode: VideoQualityMode
    message_count: Annotated[int, MaxLen(50)]
    member_count: Annotated[int, MaxLen(50)]
    thread_metadata: ThreadMetadataObject
    member: ThreadMemberObject
    default_auto_archive_duration: AutoArchiveDuration
    permissions: str
    permission_overwrites: list[OverwriteObject] = field(default_factory=list)

from dataclasses import dataclass, field
from typing import Optional, Union, Annotated

from core.objects import BaseObject
from core.objects.channel import ChannelType, ThreadMetadata, ThreadMember, AutoArchiveDuration, Overwrite
from core.objects.types import ChannelID, GuildID, MessageID, UserID, ApplicationID, CategoryID
from core.objects.user import UserObject
from core.utils.base import MaxLen


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
    rtc_region: Optional[VoiceRegion.id]
    video_quality_mode: VideoQualityMode
    message_count: Annotated[int, MaxLen(50)]
    member_count: Annotated[int, MaxLen(50)]
    thread_metadata: ThreadMetadata
    member: ThreadMember
    default_auto_archive_duration: AutoArchiveDuration
    permissions: str
    permission_overwrites: list[Overwrite] = field(default_factory=list)

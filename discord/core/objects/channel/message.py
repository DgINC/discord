from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union, Any
from typing import TYPE_CHECKING

from discord.core.objects import BaseObject

if TYPE_CHECKING:
    from discord.core.objects.application import ApplicationObject
    from discord.core.objects.channel import EmbedObject, MessageType, MessageActivity, MessageFlags, ChannelObject, \
        AttachmentObject, MessageReferenceObject, ReactionObject, ChannelMentionObject
    from discord.core.objects.guild import GuildMemberObject
    from discord.core.objects.interactions import MessageInteractionObject, MessageComponentObject
    from discord.core.objects.role import RoleObject
    from discord.core.objects.sticker import StickerItemObject, StickerObject
    from discord.core.objects.types import MessageID, ChannelID, GuildID, SnowFlake, ApplicationID
    from discord.core.objects.user import UserObject


@dataclass
class MessageObject(BaseObject):
    """
    MessageObject
    """
    id: MessageID
    channel_id: ChannelID
    guild_id: GuildID
    author: UserObject
    member: GuildMemberObject
    content: str
    timestamp: int
    edited_timestamp: Optional[Union[int, None]]
    tts: bool
    mention_everyone: bool
    mentions: list[UserObject]  # array of user objects, with an additional partial member field
    mention_roles: list[RoleObject.id]
    mention_channels: list[ChannelMentionObject]
    attachments: list[AttachmentObject]
    embeds: list[EmbedObject]
    reactions: list[ReactionObject]
    nonce: Optional[Union[int, str]]
    pinned: bool
    webhook_id: SnowFlake  # TODO: Rewrite to Webhook().id
    type: MessageType
    activity: MessageActivity
    application: ApplicationObject
    application_id: ApplicationID
    message_reference: MessageReferenceObject
    flags: MessageFlags
    referenced_message: Optional[Any] = field(hash=False, compare=False,
                                              repr=False)  # TODO: Type reference to "Message"
    interaction: MessageInteractionObject
    thread: ChannelObject
    components: list[MessageComponentObject]
    sticker_items: list[StickerItemObject]
    stickers: list[StickerObject]

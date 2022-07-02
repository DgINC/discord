from dataclasses import dataclass, field
from typing import Optional, Union, Any

from core.objects.application import ApplicationObject
from core.objects.channel import EmbedObject, MessageType, MessageActivity, MessageFlags, ChannelObject
from core.objects.channel.attachment import AttachmentObject
from core.objects.channel.messagereference import MessageReferenceObject
from core.objects.channel.reaction import ReactionObject
from core.objects.interactions import MessageInteractionObject, MessageComponentObject
from core.objects.role import RoleObject
from core.objects.sticker import StickerItemObject, StickerObject
from core.objects.user import UserObject
from discord.core.objects.channel import ChannelMention

from core.objects import BaseObject
from core.objects.guild import GuildMemberObject
from core.objects.types import MessageID, ChannelID, GuildID, SnowFlake, ApplicationID


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
    mention_channels: list[ChannelMention]
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
    referenced_message: Optional[Any] = field(hash=False, compare=False, repr=False) # TODO: Type reference to "Message"
    interaction: MessageInteractionObject
    thread: ChannelObject
    components: list[MessageComponentObject]
    sticker_items: list[StickerItemObject]
    stickers: list[StickerObject]

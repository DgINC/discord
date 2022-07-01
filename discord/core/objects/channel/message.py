from dataclasses import dataclass
from typing import Optional, Union

from core.objects.channel.attachment import AttachmentObject
from discord.core.objects.channel import ChannelMention

from core.objects import BaseObject
from core.objects.guild import GuildMemberObject
from core.objects.types import MessageID, ChannelID, GuildID


@dataclass
class MessageObject(BaseObject):
    """
    MessageObject
    """
    id: MessageID
    channel_id: ChannelID
    guild_id: GuildID
    author: User
    member: GuildMemberObject
    content: str
    timestamp: int
    edited_timestamp: Optional[Union[int, None]]
    tts: bool
    mention_everyone: bool
    mentions: list[User]  # array of user objects, with an additional partial member field
    mention_roles: list[Role.id]
    mention_channels: list[ChannelMention]
    attachments: list[AttachmentObject]
    embeds: list[Embed]
    reactions: list[Reaction]
    nonce: Optional[Union[int, str]]
    pinned: bool
    webhook_id: SnowFlake  # TODO: Rewrite to Webhook().id
    type: MessageType
    activity: MessageActivity
    application: ApplicationObject
    application_id: ApplicationID
    message_reference: MessageReference
    flags: MessageFlags
    referenced_message: Optional[Any] = field(hash=False, compare=False, repr=False) # TODO: Type reference to "Message"
    interaction: MessageInteraction
    thread: Channel
    components: list[MessageComponent]
    sticker_items: list[StickerItem]
    stickers: list[StickerObject]
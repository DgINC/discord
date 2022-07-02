from dataclasses import dataclass
from enum import Enum
from typing import Union, Final, TypeAlias

DiscordScope: TypeAlias = Final[str]


@dataclass
class AccessTokenResponse:
    access_token: str  # "6qrZcUqja7812RVdnEKjpzOL4CvHBFG"
    token_type: str  # "Bearer"
    expires_in: int  # 604800
    refresh_token: str  # "D43f5y0ahjqew82jZ4NViEr2YafMKhue",
    scope: Union[list[str], str]  # "identify"


class OAuth2Scopes(str, Enum):
    activities_read: DiscordScope = "activities.read"
    activities_write: DiscordScope = "activities.write"
    applications_builds_read: DiscordScope = "applications.builds.read"
    applications_builds_upload: DiscordScope = "applications.builds.upload"
    applications_commands: DiscordScope = "applications.commands"
    applications_commands_update: DiscordScope = "applications.commands.update"
    applications_commands_permissions_update: DiscordScope = "applications.commands.permissions.update"
    applications_entitlements: DiscordScope = "applications.entitlements"
    applications_store_update: DiscordScope = "applications.store.update"
    bot: DiscordScope = "bot"
    connections: DiscordScope = "connections"
    dm_channels_read: DiscordScope = "dm_channels.read"
    email: DiscordScope = "email"
    gdm_join: DiscordScope = "gdm.join"
    guilds: DiscordScope = "guilds"
    guilds_join: DiscordScope = "guilds.join"
    guilds_members_read: DiscordScope = "guilds.members.read"
    identify: DiscordScope = "identify"
    messages_read: DiscordScope = "messages.read"
    relationships_read: DiscordScope = "relationships.read"
    rpc: DiscordScope = "rpc"
    rpc_activities_write: DiscordScope = "rpc.activities.write"
    rpc_notifications_read: DiscordScope = "rpc.notifications.read"
    rpc_voice_read: DiscordScope = "rpc.voice.read"
    rpc_voice_write: DiscordScope = "rpc.voice.write"
    voice: DiscordScope = "voice"
    webhook_incoming: DiscordScope = "webhook.incoming"

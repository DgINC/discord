import json
from dataclasses import dataclass
from enum import IntFlag
from typing import TypeVar, final

from pydantic import BaseModel

from discord.core.objects.types.snowflake import SnowFlake
from discord.core.objects.user import User
from discord.core.objects.team import Team
from discord.core.objects.base import BaseObject

ApplicationID = TypeVar('ApplicationID', bound=SnowFlake)


@final
class ApplicationFlag(IntFlag):
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17
    GATEWAY_MESSAGE_CONTENT = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED = 1 << 19


@dataclass
class Application(BaseModel):
    id: ApplicationID
    name: str
    icon: str
    description: str
    rpc_origins: list[str]
    bot_public: bool
    bot_require_code_grant: bool
    terms_of_service_url: str
    privacy_policy_url: str
    owner: User
    summary: str
    verify_key: str
    team: Team
    guild_id: SnowFlake
    primary_sku_id: SnowFlake
    slug: str
    cover_image: str
    flags: ApplicationFlag


data = '{"bot_public":true,"bot_require_code_grant":false,"cover_image":"31deabb7e45b6c8ecfef77d2f99c81a5","description":"Test","guild_id":"290926798626357260","icon":null,"id":"172150183260323840","name":"Baba O-Riley","owner":{"avatar":null,"discriminator":"1738","flags":1024,"id":"172150183260323840","username":"i own a bot"},"primary_sku_id":"172150183260323840","slug":"test","summary":"This is a game","team":{"icon":"dd9b7dcfdf5351b9c3de0fe167bacbe1","id":"531992624043786253","members":[{"membership_state":2,"permissions":["*"],"team_id":"531992624043786253","user":{"avatar":"d9e261cd35999608eb7e3de1fae3688b","discriminator":"0001","id":"511972282709709995","username":"Mr Owner"}}]},"verify_key":"1e0a356058d627ca38a5c8c9648818061d49e49bd9da9e3ab17d98ad4d6bg2u8"}'

dictionary = json.loads(data)
print(dictionary)
#dar = Application(**dictionary)
#print(dar)
#print(type(dar))

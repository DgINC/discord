from discord.core.objects.types.base import HttpMethod


class MaxLen:
    def __init__(self, value):
        self.value = value


POST: HttpMethod = "POST"
PUT: HttpMethod = "PUT"
GET: HttpMethod = "GET"
PATCH: HttpMethod = "PATCH"
DELETE: HttpMethod = "DELETE"
OPTIONS: HttpMethod = "OPTIONS"
HEAD: HttpMethod = "HEAD"

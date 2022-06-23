import asyncio
from random import randrange
from types import SimpleNamespace

import aiohttp
from aiohttp import TraceConfig
from oauthlib.oauth2 import WebApplicationClient
from orjson import orjson

from core import OAUTH_AUTHORIZE
from core.traceconfig import on_request_start, on_request_end, on_request_exception

client = WebApplicationClient('987196221288501258')
code_verifier = client.create_code_verifier(randrange(43, 128))
code_challenge = client.create_code_challenge(code_verifier, code_challenge_method="S256")
response = client.prepare_request_uri(OAUTH_AUTHORIZE,
                                      redirect_uri='http://127.0.0.1:8080/redirect',
                                      scope=['bot', 'identify'],
                                      code_challenge=code_challenge,
                                      code_challenge_method='S256',
                                      permissions=8,
                                      state='r75fsbshassafdffs'
                                 )
print(response)


def make_trace_config(name=None) -> TraceConfig:
    def _trace_config_ctx_factory(trace_request_ctx):
        return SimpleNamespace(
            name=name,
            trace_request_ctx=trace_request_ctx
        )
    trace_config = TraceConfig(trace_config_ctx_factory=_trace_config_ctx_factory)
    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)
    trace_config.on_request_exception.append(on_request_exception)
    return trace_config


async def main():
    async with aiohttp.ClientSession(trace_configs=[make_trace_config()]) as clients:
        async with clients.get('https://discord.com/api/v10/oauth2/authorize') as resp:
            print(resp.status)
            print(await resp.json(loads=orjson.loads))

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

    loop.run_until_complete(asyncio.sleep(0.250))
    loop.close()

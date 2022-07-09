import asyncio
from types import SimpleNamespace

from aiohttp import TraceConfig

from discord.core.objects.types import HttpMethod
from discord.core.traceconfig import on_request_start, on_request_end, on_request_exception


class MaxLen:
    """
    Maxlen
    """

    def __init__(self, value):
        self.value = value


POST: HttpMethod = "POST"
PUT: HttpMethod = "PUT"
GET: HttpMethod = "GET"
PATCH: HttpMethod = "PATCH"
DELETE: HttpMethod = "DELETE"
OPTIONS: HttpMethod = "OPTIONS"
HEAD: HttpMethod = "HEAD"


def make_trace_config(name=None) -> TraceConfig:
    """

    :param name:
    :return:
    """

    def _trace_config_ctx_factory(trace_request_ctx) -> "SimpleNamespace":
        return SimpleNamespace(
            name=name,
            trace_request_ctx=trace_request_ctx
        )

    trace_config = TraceConfig(trace_config_ctx_factory=_trace_config_ctx_factory)
    trace_config.on_request_start.append(on_request_start)
    trace_config.on_request_end.append(on_request_end)
    trace_config.on_request_exception.append(on_request_exception)
    return trace_config


def synchronize_async_helper(to_await):
    """

    :param to_await:
    :return:
    """
    async_response = []

    async def run_and_capture_result():
        r = await to_await
        async_response.append(r)

    loop = asyncio.get_event_loop()
    coroutine = run_and_capture_result()
    loop.run_until_complete(coroutine)
    return async_response[0]

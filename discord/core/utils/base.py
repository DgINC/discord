from types import SimpleNamespace

from aiohttp import TraceConfig

from core.traceconfig import on_request_start, on_request_end, on_request_exception
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

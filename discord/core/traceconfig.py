from __future__ import annotations

from types import SimpleNamespace
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import TraceRequestStartParams, TraceRequestChunkSentParams, TraceResponseChunkReceivedParams, \
        TraceRequestRedirectParams, TraceRequestEndParams, TraceRequestExceptionParams, \
        TraceConnectionQueuedStartParams, \
        TraceConnectionQueuedEndParams, TraceConnectionCreateStartParams, TraceConnectionCreateEndParams, \
        TraceConnectionReuseconnParams, TraceDnsResolveHostStartParams, TraceDnsResolveHostEndParams, \
        TraceDnsCacheHitParams, TraceDnsCacheMissParams, ClientSession
    from aiohttp.tracing import TraceRequestHeadersSentParams


async def on_request_start(session: ClientSession, trace_config_ctx: SimpleNamespace, params: TraceRequestStartParams):
    print("Starting request")
    print(session)
    print(trace_config_ctx)
    print(params)
    print("--------------------------------------------------------")


async def on_request_chunk_sent(session: ClientSession,
                                trace_config_ctx: SimpleNamespace,
                                params: TraceRequestChunkSentParams):
    pass


async def on_response_chunk_received(session: ClientSession,
                                     trace_config_ctx: SimpleNamespace,
                                     params: TraceResponseChunkReceivedParams):
    pass


async def on_request_redirect(session: ClientSession,
                              trace_config_ctx: SimpleNamespace,
                              params: TraceRequestRedirectParams):
    pass


async def on_request_end(session: ClientSession,
                         trace_config_ctx: SimpleNamespace,
                         params: TraceRequestEndParams):
    print("Ending %s request for %s. I sent: %s" % (params.method, params.url, params.headers))
    print('Sent headers: %s' % params.response.request_info.headers)


async def on_request_exception(session: ClientSession,
                               trace_config_ctx: SimpleNamespace,
                               params: TraceRequestExceptionParams):
    print("Request exception")
    print(session)
    print(trace_config_ctx)
    print(params)
    print("---------------------------------------------------")


async def on_connection_queued_start(session: ClientSession,
                                     trace_config_ctx: SimpleNamespace,
                                     params: TraceConnectionQueuedStartParams):
    pass


async def on_connection_queued_end(session: ClientSession,
                                   trace_config_ctx: SimpleNamespace,
                                   params: TraceConnectionQueuedEndParams):
    pass


async def on_connection_create_start(session: ClientSession,
                                     trace_config_ctx: SimpleNamespace,
                                     params: TraceConnectionCreateStartParams):
    pass


async def on_connection_create_end(session: ClientSession,
                                   trace_config_ctx: SimpleNamespace,
                                   params: TraceConnectionCreateEndParams):
    pass


async def on_connection_reuseconn(session: ClientSession,
                                  trace_config_ctx: SimpleNamespace,
                                  params: TraceConnectionReuseconnParams):
    pass


async def on_dns_resolvehost_start(session: ClientSession,
                                   trace_config_ctx: SimpleNamespace,
                                   params: TraceDnsResolveHostStartParams):
    pass


async def on_dns_resolvehost_end(session: ClientSession,
                                 trace_config_ctx: SimpleNamespace,
                                 params: TraceDnsResolveHostEndParams):
    pass


async def on_dns_cache_hit(session: ClientSession,
                           trace_config_ctx: SimpleNamespace,
                           params: TraceDnsCacheHitParams):
    pass


async def on_dns_cache_miss(session: ClientSession,
                            trace_config_ctx: SimpleNamespace,
                            params: TraceDnsCacheMissParams):
    pass


async def on_request_headers_sent(session: ClientSession,
                                  trace_config_ctx: SimpleNamespace,
                                  params: TraceRequestHeadersSentParams):
    pass

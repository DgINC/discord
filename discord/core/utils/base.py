from aiohttp.hdrs import METH_GET, METH_PUT, METH_PATCH, METH_DELETE

class METH(str, Enum):
    METH_PUT
    METH_GET
    METH_PATCH
    METH_DELETE

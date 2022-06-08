class Guild:
    guild_id: int

    def __init__(self, guild_id: int):
        self.guild_id = guild_id

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def create(self, data: tuple):  # POST
        pass

    async def get(self):   # GET
        pass

    async def get_preview(self):   # GET
        pass

    async def modify(self):    # POST
        pass

    async def delete(self):    # DELETE
        pass

    async def get_channels(self):  # GET
        pass

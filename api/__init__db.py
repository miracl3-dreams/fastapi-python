import asyncio
from api.utils.database import engine
from api.models.admin_model import Base

async def init_db():
    async with engine.begin() as conn:
        # Uncomment the next line if you want to drop existing tables (for development)
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())

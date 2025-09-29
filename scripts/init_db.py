import asyncio
from app.db.base import Base  # Your Base that includes all models
from app.db.session import engine

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(init_models())

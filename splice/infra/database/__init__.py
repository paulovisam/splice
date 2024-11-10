from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from splice.settings import settings

# Sync
# engine = create_engine(settings.DATABASE_URL)
# def get_session():
#     with Session(engine) as session:
#         yield session

# Async
engine = create_async_engine(settings.DATABASE_URL, echo=True)


async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
# def get_session():
#     return async_session


async def get_db():
    async with async_session() as session:
        yield session

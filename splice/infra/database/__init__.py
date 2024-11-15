# from async_generator import asynccontextmanager
import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from splice.settings import settings

# Sync
# engine = create_engine(settings.DATABASE_URL)
# def get_session():
#     with Session(engine) as session:
#         yield session

# Async
engine = create_async_engine(settings.DATABASE_URL, echo=True)

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


def get_session():
    return async_session

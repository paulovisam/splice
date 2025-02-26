from contextlib import asynccontextmanager

from alembic import command
from alembic.config import Config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from splice.interface.exceptions.custom_exceptions import *
from splice.interface.exceptions.handlers import *
from splice.interface.routers.establishment_router import (
    router as establishment_router,
)
from splice.interface.routers.group_router import router as group_router
from splice.interface.routers.message_router import router as message_router
from splice.interface.routers.notification_router import (
    router as notification_router,
)
from splice.interface.routers.order_router import router as order_router
from splice.interface.routers.user_router import router as user_router
from splice.interface.routers.ws_router import router as ws_router
from splice.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Para fazer antes de iniciar
    yield
    # Desfazer


app = FastAPI(
    title="Splice API",
    version="0.1.0",
    description="",
    contact={
        "name": "Splice",
    },
    license_info={
        "name": "Nginx",
        "url": "http://nginx.org/LICENSE",
    },
    openapi_url=settings.OPENAPI_URL,
    openapi_tags=[],
    lifespan=lifespan,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(message_router)
app.include_router(ws_router)
app.include_router(group_router)
app.include_router(notification_router)
app.include_router(establishment_router)
app.include_router(order_router)


app.add_exception_handler(ValueError, invalid_value)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(BusinessException, business_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)
app.add_exception_handler(TypeError, invalid_type)


@app.get("/")
async def read_root():
    return {"message": "Olá Mundo!"}


def run_migrations():
    alembic_cfg = Config("splice/alembic.ini")
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    # Rodar as migrações antes de iniciar a aplicação
    run_migrations()

    import uvicorn

    uvicorn.run(
        "app:app",
        port=8000,
        host="0.0.0.0",
        reload=True,
        proxy_headers=True,
        forwarded_allow_ips="*",
        # log_config='log/log_config_time.ini',
    )

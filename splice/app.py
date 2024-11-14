from contextlib import asynccontextmanager

from alembic import command
from alembic.config import Config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from splice.interface.routers.user_router import router as user_router
from splice.interface.routers.ws_router import router as ws_router
from splice.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Para fazer antes de iniciar
    yield
    # Desfazer


app = FastAPI(
    title='Splice API',
    version='0.1.0',
    description='',
    contact={
        'name': 'Splice',
    },
    license_info={
        'name': 'Nginx',
        'url': 'http://nginx.org/LICENSE',
    },
    openapi_url=settings.OPENAPI_URL,
    openapi_tags=[],
    lifespan=lifespan,
)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_router)
app.include_router(ws_router)

# app.include_router([user_router, ws_router])


@app.get('/')
async def read_root():
    return {'message': 'Olá Mundo!'}


def run_migrations():
    alembic_cfg = Config('splice/alembic.ini')
    command.upgrade(alembic_cfg, 'head')


if __name__ == '__main__':
    # Rodar as migrações antes de iniciar a aplicação
    run_migrations()

    import uvicorn

    uvicorn.run(
        'main:app',
        port=8000,
        host='0.0.0.0',
        reload=True,
        proxy_headers=True,
        forwarded_allow_ips='*',
        # log_config='log/log_config_time.ini',
    )

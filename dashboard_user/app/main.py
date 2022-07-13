from fastapi import FastAPI
from app.api import user

app = FastAPI(
    version='1.0.0',
    openapi_url='/dashboard/openapi.json',
    docs_url='/dashboard/docs',
    redoc_url='/dashboard/redoc'
)

app.include_router(
    user.router,
    prefix='/user',
    tags=['User'],
    responses={418: {"description": "i'm teapot"}},
)

from fastapi import FastAPI
from app.api import user

app = FastAPI(
    version='1.0.0',
    openapi_url='/api/v1/dashboard/openapi.json',
    docs_url='/api/v1/dashboard/docs',
    redoc_url='/api/v1/dashboard/redoc'
)

app.include_router(
    user.router,
    prefix='/api/v1/user',
    tags=['User'],
    responses={418: {"description": "i'm teapot"}},
)

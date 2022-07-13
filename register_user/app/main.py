from fastapi import FastAPI
from app.api import security

app = FastAPI(
    version='1.0.0',
    docs_url='/register/docs',
    redoc_url='/register/redoc',
    openapi_url='/register/openapi.json',
)

app.include_router(
    security.security,
    prefix='/authenticate',
    tags=['Security'],
    responses={418: {"description": "i'm teapot"}},
)

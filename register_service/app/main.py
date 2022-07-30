from fastapi import FastAPI
from app.api import security
from mangum import Mangum

app = FastAPI(
    version='1.0.0',
    docs_url='/api/v1/register/docs',
    redoc_url='/api/v1/register/redoc',
    openapi_url='/api/v1/register/openapi.json',
)

app.include_router(
    security.security,
    prefix='/api/v1/authenticate',
    tags=['Security'],
    responses={418: {"description": "i'm teapot"}},
)

handler = Mangum(app)


@app.get('/api/v1/authenticate/index')
async def authenticate_index():
    return 'authenticate index'

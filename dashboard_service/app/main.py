from fastapi import FastAPI
from app.api import user
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    version='1.0.0',
    openapi_url='/api/v1/dashboard/openapi.json',
    docs_url='/api/v1/dashboard/docs',
    redoc_url='/api/v1/dashboard/redoc'
)

origins = [
    "http://localhost:80",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    user.router,
    prefix='/api/v1/user',
    tags=['User'],
    responses={418: {"description": "i'm teapot"}},
)

handler = Mangum(app)


@app.get('/')
async def index():
    return 'First page'

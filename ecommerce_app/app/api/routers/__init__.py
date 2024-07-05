from fastapi import APIRouter

from . import documents, es
from . import index

api_router = APIRouter()

api_router.include_router(
    index.router,
    prefix='/index',
    tags=["Indices"]
)

api_router.include_router(
    documents.router,
    prefix='/documents',
    tags= ["Documents"]
)

api_router.include_router(
    es.router,
    prefix='/es',
    tags=["Elastic Search"]
)


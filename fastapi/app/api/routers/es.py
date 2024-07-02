from fastapi import APIRouter, Query, Request, Response, BackgroundTasks, Depends, status
from fastapi.responses import JSONResponse


from .. import schema, services
from app.database.elasticsearch.deps import es_dependency

router = APIRouter()


@router.get('/check', status_code=status.HTTP_200_OK)
async def base(es:es_dependency):
    return {'es': await es.nodes.stats()}
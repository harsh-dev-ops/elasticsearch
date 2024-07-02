
from uuid import uuid4
from fastapi import APIRouter, Query, Request, Response, BackgroundTasks, Depends, status
from fastapi.responses import JSONResponse
from elasticsearch_dsl import AsyncSearch, Q


from .. import schema, services
from app.database.elasticsearch.deps import es_dependency

router = APIRouter()


@router.get('/all/{index}', status_code=status.HTTP_200_OK)
async def get_all_documents(request: Request, response: Response, index:str, es:es_dependency, page:int=1, size:int = 10):
    s = AsyncSearch(using=es, index=index)
    response = await s.execute()
    result = []
    
    if page - 1:
        response = response[(page-1)*size:-1]
    if size:
        response = response[:size]
        
    for hit in response:
        data = {
            **hit.to_dict(),
            "id": hit.meta.id
        }
        result.append(data)
    return result

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_index(request: Request, response: Response, data:schema.CreateIndex, es:es_dependency):
    obj = await es.index(index=data.index, document={})
    return obj
    
@router.delete('/delete/{index}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_index(request:Request, response: Response, index:str, es:es_dependency):
    obj = await es.indices.delete(index=index)    
    return obj
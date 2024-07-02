
from uuid import uuid4
from fastapi import APIRouter, Query, Request, Response, BackgroundTasks, Depends, status
from fastapi.responses import JSONResponse
from elasticsearch_dsl import AsyncSearch, Q


from .. import schema, services
from app.database.elasticsearch.deps import es_dependency

router = APIRouter()


@router.post('/create/{index}', status_code=status.HTTP_201_CREATED)
async def create_index(request: Request, response: Response, es:es_dependency, index:str, data:schema.CreateDocument):
    obj = await es.create(index=index,document=data.model_dump(), id=str(uuid4()))
    return obj

@router.get('/get/{index}', status_code=status.HTTP_200_OK)
async def get_document(request: Request, response: Response, index:str, query:str, es:es_dependency):
    s = AsyncSearch(using=es, index=index)
    
    # for key, value in data.model_dump(exclude_none=True).items():
    #     s = s.query("match", **{key: value})
    q = Q("multi_match", query=query, fields=['title', 'description'])
    s = s.query(q)
        
    response = await s.execute()
    result = []
    for hit in response:
        data = {
            **hit.to_dict(),
            "id": hit.meta.id
        }
        result.append(data)
    return result


@router.delete('/delete/{index}/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(request: Request, response: Response, index:str, id:str, es:es_dependency):
    obj = await es.delete(index=index, id=id)
    return obj
from typing import Annotated, List
from typing_extensions import Doc

from app.networks import apis
from app.conf.settings import settings
from .deps import get_token

async def auth_request(
    path: Annotated[
        str,
        Doc("Api path.")
    ],
    method: Annotated[
        str,
        Doc("get, post, put, patch, delete")
        ] = 'post',
    payload: Annotated[
        dict,
        Doc("Payload for user service.")
        ] = {},
    ) -> tuple:
    
    url = f"{settings.AUTH_SERVICE_URL}/{path}"
    response, status_code = await apis.create_request(
            url=url,
            method=method,
            payload=payload
        )
    return (response, status_code)


async def token_details(token: str):
    path = "api/tokens/details"
    response, status_code = await auth_request(path, 'post', {'access_token': token})
    return response


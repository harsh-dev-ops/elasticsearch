from fastapi import Depends
from typing import Annotated

from . import schemes, services
from ..schema import TokenDetails


get_token = Annotated[str, Depends(schemes.access_token)]

async def get_token_details(token: Annotated[str, Depends(schemes.access_token)]) -> TokenDetails:
    data = await services.token_details(token)
    return TokenDetails(**data)

token_details = Annotated[TokenDetails, Depends(get_token_details)]
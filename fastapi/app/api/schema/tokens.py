from typing import Annotated
from typing_extensions import Doc
from pydantic import BaseModel
    
class TokenDetails(BaseModel):
    sub: Annotated[str, Doc("")]
    admin: Annotated[bool, Doc("")]
    email: Annotated[str, Doc("")]
    staff: Annotated[bool, Doc("")]
    is_verfied: Annotated[bool, Doc("")]
    valid_token: Annotated[bool, Doc("")]

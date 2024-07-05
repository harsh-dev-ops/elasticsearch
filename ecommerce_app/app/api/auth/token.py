from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

from app.conf.settings import settings
from .schema import Token
from .services import auth_request

router = APIRouter()

@router.post('/auth')
async def login_access_token(
    request: Request, 
    response: Response, 
    user_form: Annotated[
        OAuth2PasswordRequestForm, 
        Depends()
        ] = None,) -> Token:
    
    payload = {
        'email': user_form.username,
        'password': user_form.password
    }
    
    resp, status_code = await auth_request(
        path=f"api/users/login",
        method='post',
        payload=payload
    )
    
    data = {
        'access_token': resp['access_token'],
        'token_type': resp['token_type']
    }
    
    return Token(**data)

        
    
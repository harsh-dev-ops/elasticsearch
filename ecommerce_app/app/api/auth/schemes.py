from fastapi.security import APIKeyHeader, OAuth2PasswordBearer

access_token = APIKeyHeader(name='X-Auth-Token')
access_token = OAuth2PasswordBearer(tokenUrl="api/auth")
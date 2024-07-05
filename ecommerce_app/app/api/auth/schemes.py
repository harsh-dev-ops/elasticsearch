from fastapi.security import APIKeyHeader

access_token = APIKeyHeader(name='X-Auth-Token')
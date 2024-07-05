from datetime import datetime
from redis_om import HashModel, Migrator, Field

from ..sessions import redis_db


class BaseModel(HashModel):
    pass
    
    class Meta:
        database = redis_db
    
Migrator().run()
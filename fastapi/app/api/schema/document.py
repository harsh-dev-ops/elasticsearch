from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any, Optional


class CreateDocument(BaseModel):
    title: str
    description: str
    
class SearchDocument(CreateDocument):
    title: Optional[str] = None
    description: Optional[str] = None
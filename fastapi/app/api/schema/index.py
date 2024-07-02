from pydantic import BaseModel
from typing import Optional, List


class CreateIndex(BaseModel):
    index: str
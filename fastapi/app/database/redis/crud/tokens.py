from .base import BaseCrud
from ..models import TokenModel

class TokenCrud(BaseCrud):
    def __init__(self, Model=TokenModel):
        super().__init__(Model)
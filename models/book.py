from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: Optional[str]
    titulo:str 
    autor:str 
    editorial:str 
    idioma:str
    precio:str 

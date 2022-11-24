from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    nombre:str
    apellido:str 
    documento:int 
    email:str
    direccion:str 
    password:str 

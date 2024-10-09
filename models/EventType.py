from pydantic import BaseModel, Field
from typing import Optional

class EventType(BaseModel):
    id: int 
    categoria: str 
    descricao: str 
    publico_alvo: str 

class EventTypeUpdate(BaseModel):
    categoria: Optional[str] 
    descricao: Optional[str] 
    publico_alvo: Optional[str] 

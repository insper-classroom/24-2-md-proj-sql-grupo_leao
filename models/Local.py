from pydantic import BaseModel, Field
from typing import Optional

class Local(BaseModel):
    id: int
    nome: str
    cidade: str 
    endereco: str
    capacidade: int 
    telefone: str 

class LocalUpdate(BaseModel):
    nome: Optional[str]
    endereco: Optional[str]
    capacidade: Optional[int] 
    telefone: Optional[str] 
    cidade: Optional[str] 

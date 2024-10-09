from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional

class Event(BaseModel):
    id: int 
    nome: str 
    descricao: str 
    data_inicio: date 
    data_fim: date 
    horario_inicio: time
    horario_fim: time 
    local: int
    tipo_evento: int 

class EventUpdate(BaseModel):
    nome: Optional[str] 
    descricao: Optional[str] 
    data_inicio: Optional[date] 
    data_fim: Optional[date] 
    horario_inicio: Optional[time] 
    horario_fim: Optional[time] 
    local: Optional[int] 
    tipo_evento: Optional[int] 

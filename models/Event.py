from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional


class Event(BaseModel):
    id: int = Field(..., title="Event ID",
                    description="Unique identifier for the event", example=1)
    nome: str = Field(..., title="Event Name",
                      description="The name of the event", example="Annual Tech Conference")
    descricao: str = Field(..., title="Event Description", description="A detailed description of the event",
                           example="A conference focused on the latest trends in technology.")
    data_inicio: date = Field(..., title="Start Date",
                              description="The starting date of the event", example="2024-11-15")
    data_fim: date = Field(..., title="End Date",
                           description="The ending date of the event", example="2024-11-17")
    horario_inicio: time = Field(..., title="Start Time",
                                 description="The starting time of the event", example="09:00")
    horario_fim: time = Field(..., title="End Time",
                              description="The ending time of the event", example="18:00")
    local: int = Field(..., title="Location",
                       description="Foreign key for the event location", example=2)
    tipo_evento: int = Field(..., title="Event Type",
                             description="Foreign key for the type of event", example=3)


class EventUpdate(BaseModel):
    nome: Optional[str] = Field(
        None, title="Event Name", description="Updated name of the event", example="Annual Tech Conference")
    descricao: Optional[str] = Field(None, title="Event Description", description="Updated description of the event",
                                     example="An updated description of the tech conference.")
    data_inicio: Optional[date] = Field(
        None, title="Start Date", description="Updated starting date of the event", example="2024-11-15")
    data_fim: Optional[date] = Field(
        None, title="End Date", description="Updated ending date of the event", example="2024-11-17")
    horario_inicio: Optional[time] = Field(
        None, title="Start Time", description="Updated starting time of the event", example="09:00")
    horario_fim: Optional[time] = Field(
        None, title="End Time", description="Updated ending time of the event", example="18:00")
    local: Optional[int] = Field(
        None, title="Location", description="Updated foreign key for the event location", example=2)
    tipo_evento: Optional[int] = Field(
        None, title="Event Type", description="Updated foreign key for the type of event", example=3)

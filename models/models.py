from sqlmodel import SQLModel, Field
from datetime import date, time
from typing import Optional


class Local(SQLModel, table=True):
    id: int = Field(..., primary_key=True, title="Event ID",
                    description="Unique identifier for the event", nullable=False)
    nome: str = Field(..., title="Location Name",
                      description="Name of the location")
    cidade: str = Field(..., title="City",
                        description="City where the location is situated")
    endereco: str = Field(..., title="Address",
                          description="Full address of the location")
    capacidade: int = Field(..., title="Capacity",
                            description="Maximum number of people the location can accommodate")
    telefone: str = Field(..., title="Phone",
                          description="Contact phone number for the location")


class LocalUpdate(SQLModel):
    nome: Optional[str] = Field(None, title="Location Name",
                                description="Updated name of the location")
    endereco: Optional[str] = Field(
        None, title="Address", description="Updated full address of the location")
    capacidade: Optional[int] = Field(
        None, title="Capacity", description="Updated maximum number of people the location can accommodate")
    telefone: Optional[str] = Field(
        None, title="Phone", description="Updated contact phone number for the location")
    cidade: Optional[str] = Field(
        None, title="City", description="Updated city where the location is situated")


class EventType(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, title="Event Type ID",
                    description="Unique identifier for the event type", nullable=False)
    categoria: str = Field(..., title="Category",
                           description="Category of the event, such as music, technology, etc.")
    descricao: str = Field(..., title="Description",
                           description="A brief description of the event type")
    publico_alvo: str = Field(..., title="Target Audience",
                              description="The target audience for the event type")


class EventTypeUpdate(SQLModel):
    categoria: Optional[str] = Field(
        None, title="Category", description="Updated category of the event type, such as music, technology, etc.")
    descricao: Optional[str] = Field(
        None, title="Description", description="Updated description of the event type")
    publico_alvo: Optional[str] = Field(
        None, title="Target Audience", description="Updated target audience for the event type")


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, title="Event ID",
                    description="Unique identifier for the event", nullable=False)
    nome: str = Field(..., title="Event Name",
                      description="The name of the event")
    descricao: str = Field(..., title="Event Description",
                           description="A detailed description of the event")
    data_inicio: date = Field(..., title="Start Date",
                              description="The starting date of the event")
    data_fim: date = Field(..., title="End Date",
                           description="The ending date of the event")
    horario_inicio: time = Field(..., title="Start Time",
                                 description="The starting time of the event")
    horario_fim: time = Field(..., title="End Time",
                              description="The ending time of the event")
    tipo_evento: Optional[int] = Field(default=None, foreign_key="eventtype.id", title="Event Type",
                                       description="Foreign key for the type of event")


class EventUpdate(SQLModel):
    nome: Optional[str] = Field(
        None, title="Event Name", description="Updated name of the event")
    descricao: Optional[str] = Field(
        None, title="Event Description", description="Updated description of the event")
    data_inicio: Optional[date] = Field(
        None, title="Start Date", description="Updated starting date of the event")
    data_fim: Optional[date] = Field(
        None, title="End Date", description="Updated ending date of the event")
    horario_inicio: Optional[time] = Field(
        None, title="Start Time", description="Updated starting time of the event")
    horario_fim: Optional[time] = Field(
        None, title="End Time", description="Updated ending time of the event")
    tipo_evento: Optional[int] = Field(
        None, foreign_key="event_type.id", title="Event Type", description="Updated foreign key for the type of event")


class LocalEventLink(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, title="LocalEvent ID",
                    description="Unique identifier for the local-event relationship", nullable=False)
    local_id: Optional[int] = Field(default=None, foreign_key="local.id", title="Local ID",
                                    description="Foreign key for the location")
    event_id: Optional[int] = Field(default=None, foreign_key="event.id", title="Event ID",
                                    description="Foreign key for the event")

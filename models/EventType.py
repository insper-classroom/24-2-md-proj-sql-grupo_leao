from pydantic import BaseModel, Field
from typing import Optional


class EventType(BaseModel):
    id: int = Field(..., title="Event Type ID",
                    description="Unique identifier for the event type", example=1)
    categoria: str = Field(..., title="Category",
                           description="Category of the event, such as music, technology, etc.", example="Technology")
    descricao: str = Field(..., title="Description", description="A brief description of the event type",
                           example="Events related to the latest advancements in technology.")
    publico_alvo: str = Field(..., title="Target Audience",
                              description="The target audience for the event type", example="Tech enthusiasts and professionals")


class EventTypeUpdate(BaseModel):
    categoria: Optional[str] = Field(
        None, title="Category", description="Updated category of the event type, such as music, technology, etc.", example="Music")
    descricao: Optional[str] = Field(None, title="Description", description="Updated description of the event type",
                                     example="Events related to music performances and concerts.")
    publico_alvo: Optional[str] = Field(
        None, title="Target Audience", description="Updated target audience for the event type", example="Music lovers of all ages")

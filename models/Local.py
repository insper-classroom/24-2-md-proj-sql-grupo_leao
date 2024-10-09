from pydantic import BaseModel, Field
from typing import Optional


class Local(BaseModel):
    id: int = Field(..., title="Location ID",
                    description="Unique identifier for the location", example=1)
    nome: str = Field(..., title="Location Name",
                      description="Name of the location", example="Convention Center")
    cidade: str = Field(..., title="City",
                        description="City where the location is situated", example="São Paulo")
    endereco: str = Field(..., title="Address", description="Full address of the location",
                          example="1234 Avenida Paulista, São Paulo, SP")
    capacidade: int = Field(..., title="Capacity",
                            description="Maximum number of people the location can accommodate", example=500)
    telefone: str = Field(..., title="Phone",
                          description="Contact phone number for the location", example="+55 11 98765-4321")


class LocalUpdate(BaseModel):
    nome: Optional[str] = Field(None, title="Location Name",
                                description="Updated name of the location", example="Expo Center")
    endereco: Optional[str] = Field(
        None, title="Address", description="Updated full address of the location", example="5678 Rua Augusta, São Paulo, SP")
    capacidade: Optional[int] = Field(
        None, title="Capacity", description="Updated maximum number of people the location can accommodate", example=1000)
    telefone: Optional[str] = Field(
        None, title="Phone", description="Updated contact phone number for the location", example="+55 11 98765-4322")
    cidade: Optional[str] = Field(
        None, title="City", description="Updated city where the location is situated", example="Rio de Janeiro")

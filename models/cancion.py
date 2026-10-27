
from typing import Optional
from pydantic import BaseModel, Field


class CancionBase(BaseModel):
    titulo: str
    duracion: int = Field(gt=0, description="Duración en segundos")
    portada_url: Optional[str] = None


class CancionID(CancionBase):
    id: int


class CancionActualizar(BaseModel):
    titulo: Optional[str] = None
    duracion: Optional[int] = Field(default=None, gt=0)
    portada_url: Optional[str] = None
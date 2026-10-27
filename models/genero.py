from typing import Optional
from pydantic import BaseModel


class GeneroBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None


class GeneroID(GeneroBase):
    id: int


class GeneroActualizar(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
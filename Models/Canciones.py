from typing import Optional
from pydantic import BaseModel
from app.enums.genero_musical import GeneroMusical


class CancionBase(BaseModel):
    titulo: str
    duracion: int
    genero: GeneroMusical
    portada_url: Optional[str] = None


class CancionID(CancionBase):
    id: int
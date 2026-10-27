from pydantic import BaseModel
from app.enums.genero_musical import GeneroMusical


class GeneroBase(BaseModel):
    nombre: GeneroMusical
    descripcion: str = ""


class GeneroID(GeneroBase):
    id: int
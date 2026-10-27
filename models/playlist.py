from typing import Optional
from pydantic import BaseModel


class PlaylistBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    usuario_id: int


class PlaylistID(PlaylistBase):
    id: int


class PlaylistActualizar(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

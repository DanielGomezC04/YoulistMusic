from typing import Optional
from pydantic import BaseModel, Field


class PlaylistBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    usuario_id: int


class PlaylistID(PlaylistBase):
    id: int
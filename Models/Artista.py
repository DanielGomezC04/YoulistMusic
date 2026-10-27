from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class ArtistaBase(BaseModel):
    nombre: str
    biografia: Optional[str] = None
    imagen_url: Optional[HttpUrl] = None


class ArtistaID(ArtistaBase):
    id: int
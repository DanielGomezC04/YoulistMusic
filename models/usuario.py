from typing import Optional
from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr


class UsuarioID(UsuarioBase):
    id: int


class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None

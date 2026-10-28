from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    estado: str = Field(default="activo", pattern="^(activo|inactivo)$")


class UsuarioID(UsuarioBase):
    id: int


class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None

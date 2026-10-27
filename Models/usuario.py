from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr


class UsuarioID(UsuarioBase):
    id: int
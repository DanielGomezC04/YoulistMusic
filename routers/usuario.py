
from fastapi import APIRouter, status, HTTPException
from data.repositories import usuarios_csv
from models.usuario import (
    UsuarioBase,
    UsuarioID,
    UsuarioActualizar
)

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=UsuarioID)
def crear_usuario(nuevo_usuario: UsuarioBase):
    datos = nuevo_usuario.model_dump(mode="json")
    return usuarios_csv.crear(datos)


@router.get("/", response_model=list[UsuarioID])
def mostrar_usuarios():
    return usuarios_csv.obtener_todos()


@router.get("/{id}", response_model=UsuarioID)
def mostrar_usuario(id: int):
    usuario = usuarios_csv.obtener_por_id(id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario


@router.patch("/{id}", response_model=UsuarioID)
def actualizar_usuario(id: int, datos: UsuarioActualizar):
    cambios = datos.model_dump(
        mode="json",
        exclude_unset=True,
        exclude_none=True
    )

    usuario = usuarios_csv.actualizar(id, cambios)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(id: int):
    eliminado = usuarios_csv.eliminar(id)

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return None

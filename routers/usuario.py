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
    usuarios = usuarios_csv.obtener_todos()
    return [
        usuario for usuario in usuarios
        if usuario.get("estado", "activo") == "activo"
    ]


@router.get("/{id}", response_model=UsuarioID)
def mostrar_usuario(id: int):
    usuario = usuarios_csv.obtener_por_id(id)

    if not usuario or usuario.get("estado", "activo") == "inactivo":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return usuario


@router.patch("/{id}", response_model=UsuarioID)
def actualizar_usuario(id: int, datos: UsuarioActualizar):
    usuario_existente = usuarios_csv.obtener_por_id(id)

    if not usuario_existente or usuario_existente.get("estado", "activo") == "inactivo":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    cambios = datos.model_dump(
        mode="json",
        exclude_unset=True,
        exclude_none=True
    )

    usuario = usuarios_csv.actualizar(id, cambios)
    return usuario


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def eliminar_usuario(id: int):
    usuario = usuarios_csv.obtener_por_id(id)

    if not usuario or usuario.get("estado", "activo") == "inactivo":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    usuarios_csv.actualizar(id, {"estado": "inactivo"})

    return {
        "mensaje": "Usuario desactivado correctamente",
        "id": id,
        "estado": "inactivo"
    }

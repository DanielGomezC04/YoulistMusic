from fastapi import APIRouter, status, HTTPException
from data.repositories import canciones_csv
from models.cancion import (
    CancionBase,
    CancionID,
    CancionActualizar
)

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CancionID
)
def crear_cancion(nueva_cancion: CancionBase):
    datos = nueva_cancion.model_dump(mode="json")
    datos["duracion"] = str(datos["duracion"])

    cancion = canciones_csv.crear(datos)
    return cancion


@router.get("/", response_model=list[CancionID])
def mostrar_canciones():
    return canciones_csv.obtener_todos()


@router.get("/{id}", response_model=CancionID)
def mostrar_cancion(id: int):
    cancion = canciones_csv.obtener_por_id(id)

    if not cancion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Canción no encontrada"
        )

    return cancion


@router.patch("/{id}", response_model=CancionID)
def actualizar_cancion(id: int, datos: CancionActualizar):
    cambios = datos.model_dump(
        mode="json",
        exclude_unset=True,
        exclude_none=True
    )

    if "duracion" in cambios:
        cambios["duracion"] = str(cambios["duracion"])

    cancion = canciones_csv.actualizar(id, cambios)

    if not cancion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Canción no encontrada"
        )

    return cancion


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cancion(id: int):
    eliminado = canciones_csv.eliminar(id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Canción no encontrada"
        )

    return None

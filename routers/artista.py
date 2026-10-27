
from fastapi import APIRouter, status, HTTPException

from data.repositories import artistas_csv
from models.artista import ArtistaBase, ArtistaID


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ArtistaID
)
def crear_artista(nuevo_artista: ArtistaBase):
    artista = artistas_csv.crear(
        nuevo_artista.model_dump(mode="json")
    )

    return artista


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ArtistaID]
)
def mostrar_artistas():
    return artistas_csv.obtener_todos()


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ArtistaID
)
def mostrar_artista(id: int):
    artista = artistas_csv.obtener_por_id(id)

    if not artista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artista no encontrado"
        )

    return artista


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ArtistaID
)
def actualizar_artista(id: int, datos: dict):
    artista = artistas_csv.actualizar(id, datos)

    if not artista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artista no encontrado"
        )

    return artista


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_artista(id: int):
    eliminado = artistas_csv.eliminar(id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artista no encontrado"
        )

    return None

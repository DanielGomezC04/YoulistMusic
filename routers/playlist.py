
from fastapi import APIRouter, status, HTTPException
from data.repositories import playlists_csv
from models.playlist import (
    PlaylistBase,
    PlaylistID,
    PlaylistActualizar
)

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=PlaylistID)
def crear_playlist(nueva_playlist: PlaylistBase):
    datos = nueva_playlist.model_dump(mode="json")
    datos["usuario_id"] = str(datos["usuario_id"])

    return playlists_csv.crear(datos)


@router.get("/", response_model=list[PlaylistID])
def mostrar_playlists():
    return playlists_csv.obtener_todos()


@router.get("/{id}", response_model=PlaylistID)
def mostrar_playlist(id: int):
    playlist = playlists_csv.obtener_por_id(id)

    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist no encontrada"
        )

    return playlist


@router.patch("/{id}", response_model=PlaylistID)
def actualizar_playlist(id: int, datos: PlaylistActualizar):
    cambios = datos.model_dump(
        mode="json",
        exclude_unset=True,
        exclude_none=True
    )

    playlist = playlists_csv.actualizar(id, cambios)

    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist no encontrada"
        )

    return playlist


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_playlist(id: int):
    eliminado = playlists_csv.eliminar(id)

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Playlist no encontrada"
        )

    return None

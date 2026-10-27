
from fastapi import APIRouter, status, HTTPException
from data.repositories import generos_csv
from models.genero import (
    GeneroBase,
    GeneroID,
    GeneroActualizar
)

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=GeneroID)
def crear_genero(nuevo_genero: GeneroBase):
    datos = nuevo_genero.model_dump(mode="json")
    return generos_csv.crear(datos)


@router.get("/", response_model=list[GeneroID])
def mostrar_generos():
    return generos_csv.obtener_todos()


@router.get("/{id}", response_model=GeneroID)
def mostrar_genero(id: int):
    genero = generos_csv.obtener_por_id(id)

    if not genero:
        raise HTTPException(
            status_code=404,
            detail="Género no encontrado"
        )

    return genero


@router.patch("/{id}", response_model=GeneroID)
def actualizar_genero(id: int, datos: GeneroActualizar):
    cambios = datos.model_dump(
        mode="json",
        exclude_unset=True,
        exclude_none=True
    )

    genero = generos_csv.actualizar(id, cambios)

    if not genero:
        raise HTTPException(
            status_code=404,
            detail="Género no encontrado"
        )

    return genero


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_genero(id: int):
    eliminado = generos_csv.eliminar(id)

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Género no encontrado"
        )

    return None

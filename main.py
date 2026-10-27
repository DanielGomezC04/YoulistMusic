from fastapi import FastAPI
from routers import artista, cancion

app = FastAPI(
)

app.include_router(
    artista.router,
    prefix="/artistas",
    tags=["Artistas"]
)

app.include_router(
    cancion.router,
    prefix="/canciones",
    tags=["Canciones"]
)


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a Spotlist"}
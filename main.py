from fastapi import FastAPI
from routers import artista, cancion, genero

app = FastAPI(
)
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a YoulistMusic"}

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

app.include_router(
    genero.router,
    prefix="/generos",
    tags=["Géneros"]
)



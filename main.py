from fastapi import FastAPI
from routers import artista

app = FastAPI(
)

app.include_router(
    artista.router,
    prefix="/artistas",
    tags=["Artistas"]
)


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a Spotlist"}
from fastapi import FastAPI
from routers import artistas

app = FastAPI(
)

app.include_router(
    artistas.router,
    prefix="/artistas",
    tags=["Artistas"]
)


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a Spotlist"}
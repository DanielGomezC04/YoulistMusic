YoulistMusic 🎵

Objetivo del proyecto

El objetivo de YoulistMusic es desarrollar una API que permita a los usuarios organizar su música favorita, registrando artistas, canciones, géneros musicales y listas de reproducción personalizadas. El proyecto busca facilitar la gestión de esta información mediante operaciones para crear, consultar, actualizar y eliminar registros, almacenando los datos en archivos CSV.

Este proyecto es una API para organizar música. Permite registrar artistas, canciones, géneros, usuarios y playlists para que cada usuario pueda crear sus propias listas de reproducción.

Diagrama de modelos

Usuario
  |
  | 1 a muchos
  v
Playlist
  |
  | Muchos a muchos
  v
Cancion -------- Artista
   |
   | Muchos a muchos
   v
 Genero

## Mapa de Endpoints

La API de YoulistMusic cuenta con endpoints para gestionar artistas, canciones, géneros musicales, usuarios y listas de reproducción. A través de estas rutas se pueden crear, consultar, actualizar y eliminar registros.

### Artistas

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/artistas/` | Crear un artista |
| GET | `/artistas/` | Consultar todos los artistas |
| GET | `/artistas/{id}` | Consultar un artista por ID |
| PATCH | `/artistas/{id}` | Actualizar un artista |
| DELETE | `/artistas/{id}` | Eliminar un artista |

### Canciones

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/canciones/` | Crear una canción |
| GET | `/canciones/` | Consultar todas las canciones |
| GET | `/canciones/{id}` | Consultar una canción por ID |
| PATCH | `/canciones/{id}` | Actualizar una canción |
| DELETE | `/canciones/{id}` | Eliminar una canción |

### Géneros

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/generos/` | Crear un género |
| GET | `/generos/` | Consultar todos los géneros |
| GET | `/generos/{id}` | Consultar un género por ID |
| PATCH | `/generos/{id}` | Actualizar un género |
| DELETE | `/generos/{id}` | Eliminar un género |

### Usuarios

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/usuarios/` | Crear un usuario |
| GET | `/usuarios/` | Consultar usuarios activos |
| GET | `/usuarios/{id}` | Consultar un usuario por ID |
| PATCH | `/usuarios/{id}` | Actualizar un usuario |
| DELETE | `/usuarios/{id}` | Desactivar un usuario y conservar su registro histórico |

### Listas de reproducción

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/playlists/` | Crear una lista de reproducción |
| GET | `/playlists/` | Consultar todas las listas |
| GET | `/playlists/{id}` | Consultar una lista por ID |
| PATCH | `/playlists/{id}` | Actualizar una lista |
| DELETE | `/playlists/{id}` | Eliminar una lista |

### inicio en visual

-it clone https://github.com/DanielGomezC04/YoulistMusic.git
-python -m venv .venv
-Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
-.\.venv\Scripts\Activate.ps1
-python -m pip install -r requirements.txt
-python.exe -m pip install --upgrade pip
-python -m uvicorn main:app --reload

Las canciones pueden tener varios artistas y géneros, y una playlist puede contener varias canciones. Un usuario puede crear varias playlists.

La información se guarda en archivos CSV y la API se desarrolla con Python y FastAPI.

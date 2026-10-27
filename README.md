YoulistMusic 🎵

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

Modelos

Usuario: nombre y correo.

Playlist: nombre, descripción y usuario al que pertenece.

Canción: título, duración y portada.

Artista: nombre, biografía e imagen.

Género: nombre y descripción.

Las canciones pueden tener varios artistas y géneros, y una playlist puede contener varias canciones. Un usuario puede crear varias playlists.

La información se guarda en archivos CSV y la API se desarrolla con Python y FastAPI.
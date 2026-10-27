import csv
from pathlib import Path


class CSVStorage:

    def __init__(self, nombre_archivo, campos):
        carpeta_proyecto = Path(__file__).resolve().parent.parent
        self.carpeta_datos = carpeta_proyecto / "data"
        self.carpeta_datos.mkdir(exist_ok=True)

        self.ruta = self.carpeta_datos / nombre_archivo
        self.campos = ["id"] + campos

        if not self.ruta.exists():
            with open(self.ruta, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(
                    archivo, fieldnames=self.campos
                )
                escritor.writeheader()

    def obtener_todos(self):
        with open(self.ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)

    def obtener_por_id(self, id_registro):
        registros = self.obtener_todos()

        for registro in registros:
            if int(registro["id"]) == id_registro:
                return registro

        return None

    def crear(self, datos):
        registros = self.obtener_todos()

        if registros:
            nuevo_id = max(
                int(registro["id"]) for registro in registros
            ) + 1
        else:
            nuevo_id = 1

        nuevo_registro = {"id": nuevo_id}

        for campo in self.campos:
            if campo != "id":
                nuevo_registro[campo] = datos.get(campo, "")

        registros.append(nuevo_registro)
        self._guardar_todos(registros)

        return nuevo_registro

    def actualizar(self, id_registro, datos):
        registros = self.obtener_todos()

        for registro in registros:
            if int(registro["id"]) == id_registro:
                for campo, valor in datos.items():
                    if campo in self.campos and campo != "id":
                        registro[campo] = valor

                self._guardar_todos(registros)
                return registro

        return None

    def eliminar(self, id_registro):
        registros = self.obtener_todos()

        nuevos_registros = [
            registro for registro in registros
            if int(registro["id"]) != id_registro
        ]

        if len(nuevos_registros) == len(registros):
            return False

        self._guardar_todos(nuevos_registros)
        return True

    def _guardar_todos(self, registros):
        with open(self.ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(
                archivo, fieldnames=self.campos
            )
            escritor.writeheader()
            escritor.writerows(registros)

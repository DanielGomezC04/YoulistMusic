from data.storage import CSVStorage

artistas_csv = CSVStorage(
    "artistas.csv",
    ["nombre", "biografia", "imagen_url"]
)
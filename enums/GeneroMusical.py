from enum import Enum


class GeneroMusical(str, Enum):
    POP = "Pop"
    ROCK = "Rock"
    REGGAETON = "Reggaeton"
    RAP = "Rap"
    ELECTRONICA = "Electronica"
    SALSA = "Salsa"
    OTRO = "Otro"
from dataclasses import dataclass

@dataclass
class ThreeDPoint:
    # Se declara poniendo solamente el tipo de variable
    x: int | float
    # Se pueden declarar también con un valor inicial
    y = 0.0
    # O se pueden usar ambos
    z: int | float = 0.0
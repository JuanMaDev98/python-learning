# Dataclasses son colecciones de clases que crean  todo automáticamente por ti, generalmente código 
# repetitivo que varia muy poco o nada (boilerplate code)

from dataclasses import dataclass

# Para usar las data clases se usa el decorador @dataclass y en vez de crear los atributos simplemente
# los defino usando type hints(sugerencias de tipos) 
# Tampoco se crea un __init__, de todo eso se encarga el decorador
@dataclass
class ThreeDPoint:
    # Se puede usar el operador de union (|) para declarar multiples tipos
    x: int | float
    y: int | float
    z: int | float
    
    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    
    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")
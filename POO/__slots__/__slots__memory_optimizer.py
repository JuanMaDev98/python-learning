# Al usar __slots__ se inhabilita el __dict__ y no se pueden crear atributos dinámicamente pero
# se ahorra memoria, muy util si creas muchos objetos de una misma clase

class Point:
    __slots__ = ("x", "y")  # Contiene una tupla con atributos válidos en formato de string

    def __init__(self, x, y):
        self.x = x
        self.y = y
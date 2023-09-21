# @cached_property hace que un metodo se ejecute una sola vez y luego cuando se llame la propiedad
# siempre retorne el mismo valor sin computar el metodo

from functools import cached_property
from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2
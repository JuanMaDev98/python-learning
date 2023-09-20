# Usando property() para crear una propiedad, asi cambiar la forma en que responde un objeto al llamar cierto atributo
# La manera mas aceptada es usando property como decorador, pero este también es código válido
class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    def _get_radius(self):
        print("Get radius")
        return self._radius
    
    def _set_radius(self, value):
        print("Set radius")
        self._radius = value
        
    def _del_radius(self):
        print("Delete radius")
        del self._radius
    
    # Puedes usar la función property() para especificar lo que pasa cuando llamas esa propiedad, usando
    # las funciones establecidas en los diferentes parámetros
    radius = property(
        fget=_get_radius,  #fget cambia el valor que devuelve usar obj.radius al valor que retorna la función dada
        fset=_set_radius,  #fset cambia usando la función dada el valor de un atributo
        fdel=_del_radius,  #fdel cambia el comportamiento al tratar de eliminar dicha propiedad
        doc="The radius property."  #muestra este docstring como el correspondiente a la propiedad
        )

circle = Circle(42.0)
print(circle.radius)
circle.radius = 20
print(circle.radius)
del circle.radius
print(circle.radius)  # Crea un error porque se acaba de eliminar la propiedad
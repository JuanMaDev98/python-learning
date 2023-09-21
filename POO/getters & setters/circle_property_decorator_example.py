# keynotes
# 1- The @property decorator must decorate the getter method.
# 2- The docstring must go in the getter method.
# 3- The setter and deleter methods must be decorated with the name of the getter method
# plus .setter and .deleter, respectively.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius


circle = Circle(42.0)
print(circle.radius)

circle.radius = 100.0
print(circle.radius)

del circle.radius
print(circle.radius)






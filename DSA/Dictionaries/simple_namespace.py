from types import SimpleNamespace

# Los SimpleNamespace son diccionarios pero que se acceden a través de atributos y tienen
# una __repr__ mas bonita, poco mas que eso
car1 = SimpleNamespace(color="red", mileage=3812.4, automatic=True)

print(car1.color)
print(car1)
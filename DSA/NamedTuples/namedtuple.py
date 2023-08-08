from collections import namedtuple

# Creo una namedtuple con 4 atributos
Column = namedtuple("Column", "id name age sex")

# Crea la namedtuple usando de plantilla Column creada anteriormente
column1 = Column(98012508987, "Juan", 25, "male")

print(column1)
# Las namedtuples pueden ser accedidas por su indice o su nombre de atributo
print(column1[1])
print(column1.name)

# Las namedtuples son utiles a la hora de organizar datos, es como crear objetos
# pero mucho mas rapido y mas memory efficient
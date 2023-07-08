a = b = c = 69  # Esto existe en python
print(a, b, c)

print(id(a))  # id() verifica que el id unico que tiene un objeto
print(id(b))
print(type(a), type(b))  # Tipo de objeto al que referencian a y b
# Aqui podemos verificar que a y b referencian ambos al mismo objeto de tipo int
print(id(a) == id(b))

print("\n")  # -------------------------------------------------------------------
x = 257
y = 257
print("x & y tienen el mismo valor pero son referencias de diferentes objetos en memoria")
print(id(x), id(y))
print(id(x) == id(y))





















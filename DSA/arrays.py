from array import *  # los array en python hay que importarlos para poder trabajar con ellos

x = array("i", [10, 20, 30])
print(x)
print(len(x))
print(x[0])
print(x.index(30))  # Si el valor no esta en la lista retorna 0
print(x[1:2])  # Se le puede hacer cortes como con otras estructuras de datos

# Conclusión: Muy parecido a las listas, con la diferencia a la hora de declarar un array
# Además solo pueden tener un ismo tipo de valor, el cual se declara al crearlas
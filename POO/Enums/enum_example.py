# Se usa para representar contantes que pueden tomar una limitada cantidad de valores (meses de año,
# dias de la semana, estaciones, etc...)
# Son constantes, por lo tanto, sus valores no pueden ser cambiados

from enum import Enum

# Se crea una clase nueva heredando la clase base Enum, para crearla con funcionalidad básica añadida    
class WeekDay(Enum):
    MONDAY = 1  # Nota que son valores constantes, por lo que el nombre va en mayúscula para seguir las convenciones
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Las Enumeraciones son iterables por defecto
for i in WeekDay:
    print(f"{i.name} --> {i.value}")

print(list(WeekDay))
# Sintaxis parecida a los diccionarios para acceder a los valores en una clase enum
print(WeekDay.MONDAY.value)
# Dot Notation
print(WeekDay.MONDAY)
# Call notation
print(WeekDay(2))
# Dictionary notation
print(WeekDay["WEDNESDAY"])



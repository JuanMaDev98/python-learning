
# Esta función devuelve el número mayor de dos números
def max_2(number1,number2):
    # Comprueba si el primer número es mayor que el segundo
    if number1 > number2:
        # Devuelve el primer número 
        return number1
    # Comprueba si el segundo número es mayor que el primero
    elif number1 < number2:
        # Devuelve el segundo número
        return number2
    else: 
        # Si los dos números son iguales, devuelve el primero
        return number1
    
# Pide al usuario que introduzca un número
x = input("Primer Número: ")
# Pide al usuario que introduzca otro número
y = input("Segundo Número: ")

# Intenta convertir los valores a enteros
try:    
    x = int(x)
    y = int(y)
# Si hay un error, muestra un mensaje de error
except:
    print("El valor introducido no es un número")
    quit()

# Llama a la función max_2 con los números introducidos por el usuario
print(max_2(x,y))



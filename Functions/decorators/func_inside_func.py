def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child  # Para retornar una función se pone en el return sin paréntesis
    else:
        return second_child


print(parent(1))
first = parent(1)  # Se puede asignar el return de la función de orden superior a una variable
second = parent(2)

print(first())  # Esa variable en este caso se vuelve una función, porque la función de orden superior retorna una función
print(second())  
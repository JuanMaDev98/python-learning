def hello():
    # Reviso si no tiene atributo data la funcion, si lo tiene lo aumento en 1 cada vez que la funcion es llamada
    if not hasattr(hello, "data"):
        hello.data = 1
    else:
        hello.data += 1
    print("Hello")


hello()
hello()
hello()
hello()
hello()
print(hello.data)
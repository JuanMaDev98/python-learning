x = input("Name: ")

# Las anotaciones en funciones son solo eso, anotaciones, el IDE las
# resalta como errores, pero el interpreter no verá problema alguno
def namer(name: int) -> str:
    print(name)


namer(x)

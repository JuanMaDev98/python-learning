from types import MappingProxyType
writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)  # crea un diccionario a partir de otro, pero este es inmutable

read_only["one"] = 23  # Devuelve un traceback porque el MappingProxyType no es editable

# Los cambios al original se reflejan en el proxy
writable["one"] = 42
print(read_only)
x = "15"

try:
    int(x)
except ValueError as error:
    print(error)
else:  # El else se ejecuta si no hay ninguna excepcion
    print("It's ok")
finally:
    print(x)
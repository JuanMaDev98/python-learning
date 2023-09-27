john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}


# Clase vacía para rellenar dinámicamente son setattr()
class Record:
    """Hold a record of data."""


john_record = Record()

# Rellenamos la clase con los valores del diccionario jhon
for field, value in john.items():
    setattr(john_record, field, value)

# Usamos el dunder __dict__ para saber todos los atributos pertnecientes a john_record
print(john_record.__dict__)
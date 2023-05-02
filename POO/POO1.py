import csv


class Animal:
    
    all_animals = []
    
    def __init__(self, name: str, age: int, color: str):
        #Comprobaciones
        assert age >= 0, "La edad de un animal no puede ser negativa"
        
        #Declaraciones
        self.name = name
        self.age = age
        self.color = color
        
        #acciones
        Animal.all_animals.append(self)
    
    def __repr__(self):
        return f'Animal("{self.name}", {self.age}, "{self.color}")'
    
    def die(self):
        Animal.all_animals.remove(self)
        del self
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("objects.csv") as x:
            items = list(csv.DictReader(x))
        
        for item in items:
            Animal(
                item.get("name"),
                int(item.get("age")), 
                item.get("color"),
                )
                
    pass


Animal.instantiate_from_csv()

print(Animal.all_animals)




















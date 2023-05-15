#Basic POO

class Dog:

    all_dogs = []
    
    def __init__(self, name: str, age: int):
        
        #comprobaciones
        assert age >= 0, "Age can't be less than 0"
        
        #asignaciones
        self._name = name
        self._age = age
        
        #acciones
        Dog.all_dogs.append(self)
        
    def bark(self):
        print(f"{self.name} barks")

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, num):
        if num >= 0:
            self._age = num
        else:
            print("Age can't be less than 0")
    
    def __repr__(self) -> str:
        return f"{self._name}"

dog1 = Dog("Dana",3)
print(dog1.name)
dog1.bark()

dog1.age = 5
print(dog1.age)

print(Dog.all_dogs)










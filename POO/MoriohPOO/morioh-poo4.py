#Classmethod & Class Attributes

class Person:
    num_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.num_people
    
    @classmethod
    def add_person(cls):
        cls.num_people += 1
        
        
p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people())
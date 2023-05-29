class User:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender 
        
    def __str__(self):
        return f'''
        Personal Details\n
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        '''

#Child Class
class Bank(User):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def show_balance(self):
        print(f"Current balance: {self.balance} BTC")
        
    def deposit(self, amount: float):
        assert amount > 0, "amount parameter can't be 0 or less"
        self.balance =+ amount
        print("Account balance has been updated")
        self.show_balance() 

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print("Account balance has been updated")
            self.show_balance() 
        else:
            print("Insufficient founds for that operation")
            self.show_balance() 
    
    def __str__(self):
        return f'''
        Personal Details\n
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        {self.show_balance()}
        '''    

    
        
johan = Bank("Johan", 21, "Male")
print(johan)
johan.deposit(10)
johan.withdraw(5)
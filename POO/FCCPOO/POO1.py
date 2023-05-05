#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Saico
#
# Created:     13/04/2023
# Copyright:   (c) Saico 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        #Run validations
        assert price >= 0, f"Price {price} can't be a negative value"
        assert quantity >=0, f"Quantity {quantity} can't be a negative value"

        #Assign properties
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): #Calculate the total price of all of this items in stock
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

# Print items attributes
item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.5
item2.apply_discount()
print(item2.calculate_total_price())



print(Item.__dict__) #All the attributes for Class level
print(item1.__dict__) #All the attributes for instance level




























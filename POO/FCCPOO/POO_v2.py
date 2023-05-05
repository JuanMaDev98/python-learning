import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} can't be a negative value"
        assert quantity >= 0, f"Quantity {quantity} can't be a negative value"

        # Assign properties
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


    def calculate_total_price(self): # Calculate the total price of all of this items in stock
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod   # Decorator que Declara que el proximo metodo es de la clase, no del objeto
    def instantiate_from_csv(cls):  # Parametro cls pasa la clase como parametro a los metodos de clase
        with open('Item.csv', 'r') as f:
            reader = csv.DictReader(f)  # Lee un csv como una lista de diccionarios
            items = list(reader)

        for item in items:
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = float(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False





    #Magic Methods
    def __repr__(self): # Magic Method for representation of the items
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(7.5))

Item.instantiate_from_csv()

print("\nLlamando a los objetos usando el metodo magico __repr__\n")
for instance in Item.all:
    print(instance)















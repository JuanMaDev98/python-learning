from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):
        # Call to super function to have access to all attributes / Methods
        super().__init__(
            name, price, quantity
        )

        # Run validations
        assert broken_phones >= 0, f"Broken phones {broken_phones} can't be a negative value"

        # Assign properties
        self.broken_phones = broken_phones

    pass

item1 = Item("MyItem", 1000, 1)

print(item1.price)
item1.apply_increment(0.2)

print(item1)


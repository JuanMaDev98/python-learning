# How to merge dictionaries, 2 ways

fruits = {"apples": 10, "oranges": 11, "pears": 9}
vegetables = {"carrots": 12, "avocado": 8, "lettuce": 8}

food = {**fruits, **vegetables}
print(food)

food = fruits | vegetables
print(food)
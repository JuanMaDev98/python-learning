# Factorial function made in recursion (There is already a built-in in module Math)
def factorial(num):
    if num <= 1:
        return 1
    return num * (factorial(num - 1))


print(factorial(4))

# Traverse a nested list using recursion
names = [
"Adam",
[
"Bob",
[
"Chet",
"Cat",
],
"Barb",
"Bert"
],
"Alex",
[
"Bea",
"Bill"
],
"Ann"
]

# Made it on first try :)
def nested_traverse(lista):
    for i in lista:
        if type(i) == list:
            nested_traverse(i)
        else: 
            print(i)

nested_traverse(names)

# Quicksort implementation using recursion

import statistics

def quicksort(numbers):
    if len(numbers) <= 1:   # Base case where the list is empty or has only one element
        return numbers
    else:
        pivot = statistics.median(     # Calculation of the pivot item by the median-of-three item method
        [
            numbers[0],
            numbers[len(numbers) // 2],
            numbers[-1]
        ]
    )
    items_less, pivot_items, items_greater = (    # Creation of the three partition list
        [n for n in numbers if n < pivot],
        [n for n in numbers if n == pivot],
        [n for n in numbers if n > pivot]
    )

    return (         # Recursive sorting and reassembly of the partition lists
        quicksort(items_less) +
        pivot_items +
        quicksort(items_greater)
    )

numbers = [12, 123, 456, 3242, 658, 9898, 345, 241, 9567, 919, 0, 5]

print(quicksort(numbers))


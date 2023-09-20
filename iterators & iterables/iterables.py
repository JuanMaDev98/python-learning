# Un iterable es un objeto el cual puedes recorrer en un loop como una lista, set o diccionario
# Para que un objeto sea iterable debe tener implementado los dunder __getitem__ y __len__
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None
    
    # Estos dunder son usados internamente por los loops para recorrer el iterable
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)

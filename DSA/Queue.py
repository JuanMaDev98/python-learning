class Queue:
    
    def __init__(self, lista) -> None:
        self.queue = lista
    
    def enqueue(self, value) -> None:
        self.queue.append(value)
        
    def dequeue(self) -> None:
        self.queue.pop(0)
    
    def __repr__(self) -> str:
        return f"{self.queue}"


lista = ["Juan", "Jose", "Pepe", "Julio", "Lorenzo"]

new_queue = Queue(lista)
print(new_queue)
new_queue.enqueue("Orlando")
print(new_queue)
new_queue.dequeue()
print(new_queue)
        
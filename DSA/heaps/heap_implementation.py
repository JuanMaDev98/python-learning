# Simple heap implementation
# (n-1) // 2
# (n * 2) + 1 & (n*2) + 2


class Heap:
    def __init__(self, heap: list) -> None:
        self.heap = heap

    def __repr__(self) -> str:
        return str(self.heap)
    
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if self.heap[index] < self.heap[parent] and parent >= 0:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)
    
    

heap1 = Heap([1, 2, 3, 4, 5, 6, 7, 8, 0])
heap1._bubble_up(8)
print(heap1)

# Hacer lo de pop del top para priority queue, el bubble up, el heapify y un método para comprobar si una lista es un heap
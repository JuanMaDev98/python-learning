# Iterator creado como ejemplo, sirve obviamente para iterar "sequence"
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
    def __iter__(self):  # Siempre __iter__ devuelve self
        return self
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration  # Solo se detiene el iterator al alcanza este StopIteration error

x = SequenceIterator([1,2,3,4,5])

for i in x:
    print(i)
    
    
# Función generadora para generar iteraciones
def sequence_generator(sequence):
    for item in sequence:
        yield item

for i in sequence_generator(["a", "b", "c", "d"]):
    print(i)

#Expresiones generadoras (Como List Comprehension pero con paréntesis para generar iteradores)
generator_expression = (item for item in [1, 11, 111, 1111])
for i in generator_expression:
    print(i)

# Si creas un iterator y lo usas, lo agotas, esto significa que no puedes usarlo mas a no ser que crees una 
# nueva instancia de ese iterator. Tampoco puedes reiniciar un iterator

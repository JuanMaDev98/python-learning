from collections import deque

# append y pop funcionan exactamente como las listas regulares
llist = deque("abcde")
print(llist)
llist.append("f")
print(llist)
llist.pop()
print(llist)

llist.appendleft("z")  # append pero a la izquierda de la lista en vez de al final
print(llist)

llist.popleft()  # pop pero al inicio de la lista en vez de al final
print(llist)












lista = [1, 1, 3, 3, 3, 4]
dic = {}
for i in lista:
    dic[i] = dic.get(i,0) + 1

print(dic) 
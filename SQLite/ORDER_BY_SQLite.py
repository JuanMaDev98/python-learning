import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")#Ordena la lista por el rowid de manera descendente (DESC)
#No hay que poner ASC para ascendente obligatoriamente, ya que es el valor por defecto

items = c.fetchall()

for item in items:
    print(item)


#ORDER BY no modifica la base de datos sino que selecciona los elementos de la misma de manera ordenada



#conn.commit() #No se hacen cambios asi que no hay que darle commit
conn.close()

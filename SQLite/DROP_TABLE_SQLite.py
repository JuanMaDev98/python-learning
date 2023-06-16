import sqlite3

conn = sqlite3.connect("customer.db")# Conecta con el archivo de base de datos llamado customer.db, si no existe lo crea en blanco

#Crea un cursor para usar nuestra base de datos
c = conn.cursor()

#CUIDADO, BORRARÁ LA TABLA PARA SIEMPRE!!!!!!!!!!!!
c.execute("DROP TABLE customers")#Elimina la tabla customers


c.execute("SELECT * FROM customers")#Retorna error porque la tabla no existe
print(c.fetchall())

conn.commit() #Se hacen cambios asi que hay que darle commit
conn.close()

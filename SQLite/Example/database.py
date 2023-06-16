import sqlite3


#Muestra todos los valores en la Database
def show_all():
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    #Realiza los cambios y cierra la conexion
    conn.commit()
    conn.close


#Adiciona una fila a la Database
def add_one(first, last, email):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    #Realiza los cambios y cierra la conexion
    conn.commit()
    conn.close


#Adiciona muchos elementos aen forma de filas a la Database
def add_many(lista):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (lista))

    #Realiza los cambios y cierra la conexion
    conn.commit()
    conn.close


#Borra una fila de la base de datos
def delete_one(id):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)

    #Realiza los cambios y cierra la conexion
    conn.commit()
    conn.close



















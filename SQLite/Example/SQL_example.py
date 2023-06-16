import database

#database.add_one("Juan", "Gonzalez", "juanmgv98@gmail.com")

database.delete_one("6")#Se pasa como string aunque sea Int, cosas de SQL

stuff = [
    ("User1", "Lastname1", "email1"),
    ("User2", "Lastname2", "email2"),
    ("User3", "Lastname3", "email3"),
    ("User4", "Lastname4", "email4"),
    ("User5", "Lastname5", "email5"),
]

database.add_many(stuff)

database.show_all()
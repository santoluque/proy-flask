import sqlite3

connection = sqlite3.connect('mydb.db')


with open('base_dll.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO cliente (name, lastname) VALUES (?, ?)",
            ('Santiago', 'Guerrero')
            )

cur.execute("INSERT INTO cliente (name, lastname) VALUES (?, ?)",
            ('Alex', 'Sevilla')
            )

connection.commit()
connection.close()
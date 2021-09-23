import sqlite3


def create_table():
    conection = sqlite3.connect("lite.db")
    cursor = conection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conection.commit()
    conection.close()


def insert(item, quantity, price):
    conection = sqlite3.connect("lite.db")
    cursor = conection.cursor()
    cursor.execute(f"INSERT INTO store VALUES ('{item}', {quantity}, {price})")
    conection.commit()
    conection.close()


def view():
    conection = sqlite3.connect("lite.db")
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    cursor.close()
    return rows


print(view())

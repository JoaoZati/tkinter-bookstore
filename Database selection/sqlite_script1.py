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


def delete_item(item):
    conection = sqlite3.connect("lite.db")
    cursor = conection.cursor()
    cursor.execute(f"DELETE FROM store WHERE item='{item}'")
    conection.commit()
    conection.close()


def update_item(item, quantity, price):
    conection = sqlite3.connect("lite.db")
    cursor = conection.cursor()
    cursor.execute(f"UPDATE store SET quantity={quantity}, price={price} WHERE item='{item}'")
    conection.commit()
    conection.close()


#insert('Wine Glass', 10, 5.5)
#update_item('Wine Glass', 8, 5.8)
# delete_item("Wine Glass")
print(view())

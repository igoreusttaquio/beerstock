import sqlite3

def create():
    connection = sqlite3.connect('stock.db')
    cursor = connection.cursor()

    query = "CREATE TABLE IF NOT EXISTS beers (id INTEGER PRIMARY KEY, name VARCHAR(100), style VARCHAR(25), price REAL, stock INT)"
    cursor.execute(query)

    query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(80), password VARCHAR(100), active VARCHAR(1))"
    cursor.execute(query)

    connection.commit()
    connection.close()
    cursor = None


if __name__ == '__main__':
    create()
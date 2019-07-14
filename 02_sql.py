import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 270000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000),
            ]

    cursor.executemany('INSERT INTO population VALUES(?,?,?)', cities)

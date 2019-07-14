import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a table
    c.execute("""
        CREATE TABLE inventory
        (make TEXT, model TEXT, quantity INT)
        """)

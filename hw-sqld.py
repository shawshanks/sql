import sqlite3

with sqlite3.connect("cars.db") as connection:
    # create a cursor object to execute SQL commands
    c = connection.cursor()

    # retrive records that are for Ford vehicles.
    c.execute("SELECT * FROM inventory WHERE make='Ford'")
    rows = c.fetchall()
    for r in rows:
        print(r)


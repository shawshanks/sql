# UPDATE statement

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE inventory SET quantity=15 WHERE model='Focus'")
    c.execute("UPDATE inventory SET quantity=16 WHERE model='Civic'")

    print("\nNew Data:\n")

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()

    for r in rows:
        print(r)


# soloution to Page 69 second
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()
    for row in rows:
        print(f"{row[0]}, {row[1]}")
        print(f"quantity: {row[2]}")

        c.execute("SELECT count(order_date) FROM orders \
            WHERE make=? and model=?", (row[0], row[1]))
        order_count = c.fetchone()[0]

        print(order_count)
        print()


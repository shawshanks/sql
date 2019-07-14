import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""
        SELECT inventory.make, inventory.model,
                inventory.quantity, orders.order_date
        FROM inventory
        INNER JOIN orders ON
        inventory.model = orders.model
        """)

    rows = c.fetchall()
    for r in rows:
        print(f"make: {r[0]}, model: {r[1]}")
        print(f"quantity: {r[2]}")
        print(f"order_date: {r[3]}")
        print()

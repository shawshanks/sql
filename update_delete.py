import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data
    c.execute(
        """
        UPDATE population SET population = 90000
        WHERE city='New York City'
        """
        )

    # delete data
    c.execute("DELETE FROM population WHERE city='Boston'")

    print("\nNEW DATA:\n")

    c.execute("SELECT * FROM population")

    rows = c.fetchall()

    for r in rows:
        print(r)

# SELECT sqlite3

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use a for loop to iterate the database, printing the result line
    # by line

    # or c.fetchall()
    for row in c.execute("SELECT firstname, lastname from employees"):
        print(row)

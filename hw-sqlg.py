# COUNT function

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # # find each of model
    # c.execute("SELECT DISTINCT model FROM orders")

    # row = c.fetchall()
    # print(row)

    # create a dictionary of sql query
    sql = {
        'Focus count': "SELECT count(make) FROM orders WHERE model='Focus'",
        'Civic count': "SELECT count(make) FROM orders WHERE model='Civic'",
        'Ranger count': "SELECT count(make) FROM orders WHERE model='Ranger'",
        'Accord count': "SELECT count(make) FROM orders WHERE model='Accord'",
        'Avenger count': "SELECT count(make) FROM orders WHERE model='Avenger'"
    }

    for keys, values in sql.items():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print(f"{keys}: {result[0]}")


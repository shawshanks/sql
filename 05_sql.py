import sqlite3

with sqlite3.connect("new.db") as connection:
    # create a cursor object to execute SQL commands
    c = connection.cursor()

    # insert mutiple records using a tuple
    cities = (
                ('Boston', 'MA', 600000),
                ('Los Angeles', 'CA', 38000000),
                ('Houston', 'TX', 21000000),
                ('Houston', 'TX', 2100000),
                ('Houston', 'TX', 2100000),
                ('Philadelphia', 'PA', 1500000),
                ('San Antonio', 'TX', 1400000),
                ('San Diego', 'CA', 130000),
                ('Dallas', 'TX', 1200000),
                ('San Jose', 'CA', 900000),
                ('Jacksonville', 'FL', 800000),
                ('Indianapolis', 'IN', 800000),
                ('Austin', 'TX', 800000),
                ('Detroit', 'MI', 700000),
                )

    c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)


    c.execute("SELECT * FROM population WHERE population > 1000000")

    rows = c.fetchall()

    for r in rows:
        print(r)

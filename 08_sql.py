# JOINing data from multiplue tables

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""
        SELECT population.city, population.population, regions.region
        FROM population, regions
        WHERE population.city = regions.city""")

    rows = c.fetchall()
    for r in rows:
        print(r)

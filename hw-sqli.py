# page 70 First Script
import sqlite3
import random


with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE rand_int(integer INT)")

    num = [(random.randint(0, 100),) for _ in range(100)]

    c.executemany("INSERT INTO rand_int VALUES(?)", num)



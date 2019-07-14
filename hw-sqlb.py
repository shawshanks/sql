import sqlite3

# create a connection object
connection = sqlite3.connect("cars.db")

# create a cursor object to execute SQL commands
cursor = connection.cursor()

# insert data
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 10)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 11)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', 12)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 13)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Avenger', 14)")

connection.commit()
connection.close()

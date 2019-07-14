import sqlite3

# Prompting user to select a function from AVG(1),MAX(2), MIN(3), SUM(4)
# If user input 5, stand for exit.
# If user input other number, prompt user the input is error, and input the
# right number.
while True:
    num = int(input("Please input a integer--AVG(1),MAX(2), MIN(3), SUM(4): "))
    if num == 5:
        break
    elif num < 1 or num > 4:
        print("please input valid integer")
        print()
    # else:
    #     with sqlite3.connect("newnum.db") as connection:
    #         c = connection.cursor()
    #         # Four kinds of sql queries
    #         sql = (
    #                 "SELECT avg(integer) FROM rand_int",
    #                 "SELECT max(integer) FROM rand_int",
    #                 "SELECT min(integer) FROM rand_int",
    #                 "SELECT sum(integer) FROM rand_int",
    #                )

    #         c.execute(sql[num-1])
    #         result = c.fetchone()
    #         print(result[0])
    #         print()

    # other ways
    if num in set([1, 2, 3, 4]):
        with sqlite3.connect("newnum.db") as connection:
            c = connection.cursor()

            # parse the corresponding operation text
            operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[num]

            # retrieve data
            c.execute(f"SELECT {operation}(integer) FROM rand_int")

            # fetchone() retrieves one record from the query
            result = c.fetchone()

            # output reslut to screen
            print(result[0])




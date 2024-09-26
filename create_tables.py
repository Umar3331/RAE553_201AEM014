import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

#this is the only place where int vs INTEGER matters-in auto-increamenting columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #ID starts with 1, 2, 3 and so on.
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEy, price real)"
cursor.execute(create_table) #execute the table

cursor.execute("INSERT INTO items VALUES ('test', 10.99)")# adding some data

connection.commit()

connection.close()

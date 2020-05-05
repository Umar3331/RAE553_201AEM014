import sqlite3 #Importing necessary library

connection = sqlite3.connect('data.db') #Calling database data.db

cursor = connection.cursor() #This will actually work like a cursor in PC

create_table = "CREATE TABLE users (id int, username text, password text)"#Creating the table headings
cursor.execute(create_table)#Executing the table

users = [                         #creating Users table
         (1, 'Umar', '98765'),
         (2, 'Mohammad', '12345'),
         (3, 'Dom', 'Crack'),
         (4, 'Super', 'Man'),
         (5, 'Noob', 'Started')
]

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)
#instead of executing single executemany will
#execute more than one

connection.commit()#For accepting to save the data and the changes that are  done
connection.close()#For closing the connection

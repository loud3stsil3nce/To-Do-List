import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="rafi",
    passwd="root",
    database="ToDoList"
)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE ToDoList")

#mycursor.execute("CREATE TABLE ToDo (Item VARCHAR(100), Description VARCHAR(100), Status VARCHAR(10), itemID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("DROP TABLE ToDo")
#mycursor.execute("INSERT INTO ToDo (Item, Description, Status) VALUES (%s,%s,%s)", ("TOOOO", "Test Description", "IP"))
#db.commit()

#mycursor.execute("SELECT * FROM ToDo")

#for x in mycursor:
    #print(x)
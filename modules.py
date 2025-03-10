from pathlib import Path
import db

taskname = ''
description = ''
ToDo = [{'first':'item'}, ]
task = {'first':'item'}
num = len(ToDo)

cursor = db.mycursor
database = db.db



def menu():
    try:
        action = int(input("What would you like to do?\n1)View tasks\n2)Add Tasks\n3)Remove Tasks: "))
        print("")
    except ValueError:
        action = int(input("Please type in a valid number:\n1)View tasks\n2)Add Tasks\n3)Remove Tasks: "))
        print("")
    return action
def asktask():
    global taskname
    taskname = input("What is the name of your new task?\n")
    return taskname

def askdescription():
    global description
    description = input("Description of task (press enter if N/A):\n")
    return description

def addtask(name, description):
    global ToDo
    task = {}
    task[f"{name}"] = description
    ToDo.append(task)
    cursor.execute("INSERT INTO ToDo (Item, Description, Status) VALUES (%s,%s,%s)", (name, description, "IP"))
    database.commit()

def viewalltasks():
    cursor.execute("SELECT * FROM ToDo")
    rows = cursor.fetchall()
    num = 1
    for row in rows:
        print(f"{num}. {row[0]}\n{row[1]}\nStatus: {row[2]}\nTask ID: {row[3]}\n")
        num += 1
        
        
       

def remove(taskkey):
    cursor.execute("DELETE FROM ToDo WHERE itemID LIKE (%s)", (taskkey,))
    database.commit()
    
      
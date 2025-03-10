from pathlib import Path
import modules
menu = modules.menu
viewalltasks = modules.viewalltasks
addtask = modules.addtask
asktask = modules.asktask
askdescription = modules.askdescription
remove = modules.remove














def main():
    while True:
        action = menu() 
        if action == 1:
            print("\n\n")
            viewalltasks()
            print("\n\n")
        if action == 2:
            print("\n\n")
            addtask(asktask(), askdescription())
            print("\n\n")
        if action == 3:
            print("\n\nRemove a Task-- \nHere are your tasks:\n")
            viewalltasks()
            
            try:
                removedTask = int(input("Type the ItemID of the task you'd like to remove:\n"))
            except ValueError:
                removedTask = int(input("Please type in a valid ItemID number for the task you'd like to remove:\n"))
            
            remove(removedTask)
            print("\n\n")
main()
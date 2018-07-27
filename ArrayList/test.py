
import ArrayList


AL = ArrayList.ArrayList()
def printMenu():
    print("Commands:")
    print("Enter a to add\nEnter r to remove\nEnter p to display contents")
    print("Enter Q to quit")
    command = input("Please enter a command: ")
    
    return command

def insert():
    number = int(input("Enter a number to add: "))
    AL.add(number)
    print(str(number) + " added")
    print("List state is now:")
    display()


def display():
    if AL.count == 0:
        print("The list is empty.")
    else:
        print(AL)

def remove():
    print(AL)
    index = int(input("Enter index of item to remove: "))
    if AL.remove(index):
        print("Item removed, state of List is now: \n" + str(AL))
    else:
        print("Remove unsuccessful! Invalid Index")

def main():
    
    print("Now running interface for ArrayList...")
    command = ""
    while True:
        command = printMenu()
        if command == "Q":
            break
        elif command == "a":
            insert()
        elif command == "r":
            remove()
        elif command == "p":
            display()
        else:
            print("Incorrect command!")

        print()
main()

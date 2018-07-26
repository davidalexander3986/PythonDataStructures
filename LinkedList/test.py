import LinkedList
""" This program tests my linked list, by providing a command line interface"""


LL = LinkedList.LinkedList()
def printMenu():
    print("Commands:")
    print("Enter i to insert\nEnter r to remove\nEnter p to display contents")
    print("Enter Q to quit")
    command = input("Please enter a command: ")
    
    return command

def insert():
    number = int(input("Enter a number to insert: "))
    LL.insert(number)
    print(str(number) + " inserted")
    print("List state is now:")
    display()


def display():
    if LL.count == 0:
        print("The list is empty.")
    else:
        print(LL)

def remove():
    print(LL)
    index = int(input("Enter index of item to remove: "))
    LL.remove(index)

    print("State of List is now: ")
    print(LL)

def main():
    
    print("Now running interface for Linked List...")
    command = ""
    while True:
        command = printMenu()
        if command == "Q":
            break
        elif command == "i":
            insert()
        elif command == "r":
            remove()
        elif command == "p":
            display()
        else:
            print("Incorrect command!")

        print()
main()

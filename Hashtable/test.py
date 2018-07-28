
"""Here, I test my implementation of a hashtable by applying a command-line 
interfface """

import hash as ht

HT = ht.Hashtable()

def printMenu():
    print("Commands:")
    print("\tEnter i to insert\n\tEnter l to lookup\n\tEnter d to display contents")
    print("\tEnter Q to quit")
    command = input("Please enter a command: ")
    
    return command

def insert():
    key = int(input("Enter the key for the new data: "))
    data = input("Enter the data: ")

    HT.insert(key, data)
    print(str(data) + " added")
    display()

def lookup():
    key = int(input("Please enter key of data: "))
    data = HT.lookup(key)
    print("Data at key " + str(key) +  " is " + str(data))

def display():
    if HT.size() == 0:
        print("The table is empty.")
    else:
        print(HT)

def main():
    
    print("Now running interface for Hashtable...")
    command = ""
    while True:
        command = printMenu()
        if command == "Q":
            break
        elif command == "i":
            insert()
        elif command == "l":
            lookup()
        elif command == "d":
            display()
        else:
            print("Incorrect command!")

        print()
main()


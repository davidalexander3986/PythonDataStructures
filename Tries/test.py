import Trie as TST

TST = TST.Trie()

def printMenu():
    print("Commands:")
    print("\tEnter i to insert\n\tEnter l to lookup")
    print("\tEnter Q to quit")
    command = input("Please enter a command: ")
    
    return command

def insert():
    string = input("Enter a string to insert: ")
    TST.insert(string)

    print(string + " added.")

def lookup():
    search = input("Enter a string for me to lookup: ")
    result = TST.lookup(search)

    if result:
        print("String found!!!")
    else:
        print("String NOT found!!!")

def main():
    print("Now running interface for Ternary Search Trie...")
    command = ""
    while True:
        command = printMenu()
        if command == "Q":
            break
        elif command == "i":
            insert()
        elif command == "l":
            lookup()
        else:
            print("Incorrect command!")

        print()
main()


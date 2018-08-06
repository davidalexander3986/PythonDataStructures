import SimpleStack as st

ST = st.Stack()

def printMenu():
    print("Commands:")
    print("Enter p to push\nEnter po to pop\nEnter pe to peek\nEnter d to display contents")
    print("Enter Q to quit")
    command = input("Please enter a command: ")
    
    return command

def push():
    number = int(input("Enter a number to push: "))
    ST.push(number)
    print(str(number) + " PUSHED to stack")
    print("Stack is now:")
    display()

def peek():
    thing = ST.peek()
    if thing == None:
        print("Nothing to PEEK")
    else:
        print(str(thing))

def display():
    print(ST)

def pop():
    itemPopped = ST.pop()
    if itemPopped == None:
        print("Nothing to pop!")
    else:
        print(str(itemPopped) + " POPPED from stack")
    print("Stack is now: ")
    print(ST)

def main():
    
    print("Now running interface for Stack...")
    command = ""
    while True:
        command = printMenu()
        if command == "Q":
            break
        elif command == "p":
            push()
        elif command == "po":
            pop()
        elif command == "pe":
            peek()
        elif command == "d":
            display()
        else:
            print("Incorrect command!")

        print()
main()

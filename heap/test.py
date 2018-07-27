
import priorityQueue as pq

PQ = pq.PriorityQueue()

def printMenu():
    print("Commands:")
    print("\tEnter a to add\n\tEnter p to pop\n\tEnter d to display contents")
    print("\tEnter t to top\n\tEnter Q to quit")
    command = input("Please enter a command: ")
    
    return command

def add():
    number = int(input("Enter a number to add: "))
    PQ.push(number)
    print(str(number) + " added")
    print("priority queue state is now:")
    display()

def pop():
    print(PQ)
    item = PQ.pop()
    print("Item removed was " + str(item))
    display()

def display():
    if PQ.size() == 0:
        print("The priority queue is empty.")
    else:
        print(PQ)

def top():
    if PQ.size() == 0:
        print("The priority queue is empty")
    else:
        print("The top element is " + str(PQ.peek()))

def main():
    
    print("Now running interface for Priority Queue...")
    command = ""
    while True:
        command = printMenu()
        if command == "Q":
            break
        elif command == "a":
            add()
        elif command == "p":
            pop()
        elif command == "t":
            top()
        elif command == "d":
            display()
        else:
            print("Incorrect command!")

        print()
main()

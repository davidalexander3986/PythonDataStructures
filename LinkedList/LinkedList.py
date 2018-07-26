import Node

""" This is the class for my Linked List data structure, which I made by 
    remembering what I was taught, and referring to sources I used in 
    my freshman year of college."""

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, data):
        """Inserts a new Node at head, increments the count """
        temp = self.head
        self.head = Node.Node(data)
        self.head.next = temp
        self.count += 1

    def remove(self, index):
        """ Removes a Node at specified index"""
        if index == 0:
            self.head = self.head.next
        else:
            # Iterate until reaching the node before the node to remove
            curr = self.head
            for i in range(index-1):
                curr = curr.next

            temp = curr.next
            curr.next = temp.next
        self.count -= 1
    
    def get(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.getData()


    def change(self, index, data):
        """Changes data stored at a specified index"""
        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.data = data


    def __str__(self):
        toReturn = "Count: " + str(self.count) + "\n"
        toReturn += "[ "
        for i in range(self.count):
            toReturn += str(self.get(i))
            if i != self.count - 1:
                toReturn += ", "
        
        toReturn += " ]"
        return toReturn





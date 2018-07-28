"""My implementation of HashTable uses a Linked List (my own Linked List) to 
in the form of seperate chaining, to resolve conflicts. """

import Bucket as B

class Hashtable:

    def __init__(self):
        self.capacity = 10
        self.table = [None] * self.capacity
        self.occupancy = 0

    def hash_function(self, key):
        return (key ** 2) % self.capacity

    def insert(self, key, data):
        index = self.hash_function(key)
        
        if self.table[index] == None:
            self.table[index] = B.Bucket(key, data)
        else:
            self.table[index].addSibling(key, data)

        self.occupancy += 1

    def lookup(self, key):
        index = self.hash_function(key)
        foundStuff = self.find(index, key)
        return foundStuff


    def find(self, index, key):
        curr = self.table[index]
        while curr != None:
            if curr.getKey() == key:
                return curr.getData()
            else:
                curr = curr.next
        return None


    def __str__(self):
        string = "Occupancy: " + str(self.occupancy) + "\n"
        for thing in self.table:
            print(thing)
        return string

    def size(self):
        return self.occupancy







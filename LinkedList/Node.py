""" Node class which will be used in LinkecList """
class Node:
    
    def __init__(self, stuff):
        self.data = stuff
        self.next = None

    def insertNext(self, newNode):
        temp = self.next
        self.next = newNode
        newNode.next = temp

    def change(self, newData):
        self.data = newData

    def getData(self):
        return self.data


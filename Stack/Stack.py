import StackNode as SN
class Stack:

    def __init__(self):
        self.top = None

    def pop(self):
        if top == None:
            return None
        else:
            toReturn = self.top.data
            self.top = self.top.next
            return toReturn

    def push(self, thing):
        oldTop = self.top
        self.top = StackNode(thing)
        self.top.next = oldTop

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.top == None


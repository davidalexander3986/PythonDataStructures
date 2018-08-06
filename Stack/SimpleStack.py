"""Implementation for my own stack data structure """

class Stack:
    
    def __init__(self):
        self.items = []
        self.count = 0
        self.stackptr = -1

    def push(self, data):
        self.items.append(data)
        self.count += 1
        self.stackptr += 1

    def pop(self):
        if self.count > 0:
            toReturn = self.items[self.stackptr]
            self.stackptr -= 1
            self.count -= 1
        else:
            toReturn = None
        return toReturn

    def peek(self):
        return self.items[self.stackptr]

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def __str__(self):
        toReturn  = ""
        if self.count > 0:
            strPtr = self.stackptr
            toReturn += "TOP:\t"
            while strPtr > -1:
                toReturn += str(self.items[strPtr]) + "\n\t"
                strPtr -= 1
        else:
            toReturn += "STACK IS EMPTY"

        return toReturn
                

            

        

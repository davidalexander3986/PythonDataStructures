"""This class is used in implementing the Hashtable with seperate chaining 
as the collision resolution"""

class Bucket:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


    def addSibling(self, key, data):
        if self.next == None:
            self.next = Bucket(key, data)
        else:
            self.next.addSibling(key,data)



    def getKey(self):
        return self.key

    def getData(self):
        return self.data

    def __str__(self):
        string = str(self.key) + " ---> " + str(self.data)
        if self.next != None:
            string += ", " + str(self.next)
        
        return string

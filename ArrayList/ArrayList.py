"""
This is the implementation for an arraylist in Python. Since Python doesn't 
have arrays, this isn't a "true" arraylist, because the backend is using a list
object, which is itself similar to an ArrayList. My algorithm is a bit complex, 
since I decided to add in my own remove feature, to conserve space. Whenever
an item is removed, the index of that item is added to a list of open indices
(openSlots). Whenever an item is added, this list is consulted first, before 
either adding data to the next open slot, or resizing. Also, this avoids the 
bug that could occur when you remove an element that's not at the end of 
the list. This would decrement count, but then when you add a new element, 
it could overwrite data stored at the index of count. 
"""

class ArrayList:

    def __init__(self):
        self.capacity = 2
        self.data = [None] * self.capacity
        self.openSlots = []
        self.count = 0


    def add(self, data):
        """First, checks if an empty slot exists, than either appends or
            resizes"""
        if self.count == self.capacity:
            self.resize()
        if len(self.openSlots) > 0:
            self.data[self.openSlots[0]] = data
            del self.openSlots[0]
        else:
            self.data[self.count] = data

        self.count += 1


    def resize(self):
        oldCap = self.capacity
        self.capacity *= 2
        newData = [None] * self.capacity
        
        for i in range(oldCap):
            newData[i] = self.data[i]
        self.data = newData
        
    def remove(self,index):
        if index < self.capacity:
            if self.data[index] != None:
                self.data[index] = None
                self.openSlots.append(index)
                self.count -= 1
                return True
            else:
                return False
        else:
            return False


    def get(self, index):
        if index < self.count:
            return self.data[index]
        else:
            return None

    def size(self):
        return self.count

    def __str__(self):
        string = "Capacity: " + str(self.capacity) + "\t\tSize: " + \
            str(self.count) + "\nIndex\t\tValue\n"
        ind = 0
        for thing in self.data:
            string += str(ind) + "\t\t" + str(thing) + "\n"
            ind += 1
        string += "\n"
        return string




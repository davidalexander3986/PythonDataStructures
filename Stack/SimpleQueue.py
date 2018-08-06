
class Queue:

    def __init__(self):
        self.count = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.count += 1

    def remove(self):
        if self.count > 0:
            toReturn = self.items[0]
            del self.items[0]
            self.count -= 1
            return toReturn
        else:
            return None
    def peek(self):
        if self.count > 0:
            return self.items[0]
        else:
            return None

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False
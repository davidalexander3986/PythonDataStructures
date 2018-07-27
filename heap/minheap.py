""" My implementation of a heap tree, using a list as a backend structure"""
class minHeap:

    def __init__(self):
        self.heap = []
        self.count = 0

    def heapify(self, index):
        """After adding an element, this function is called on that element's 
        index to trickle it up, if necessary """
        parentIndex = self.parent(index)
        if parentIndex == -1:
            return
        else:
            parent = self.heap[parentIndex]
            if parent > self.heap[index]:
                self.swap(parentIndex, index)
                self.heapify(parentIndex)
        


    def add(self, data):
        self.heap.append(data)
        self.heapify(self.count)
        self.count += 1


    def getMin(self):
        if self.count == 0:
            return None
        return self.heap[0]

    def removeMin(self):
        if self.count == 0:
            return None
        root = self.heap[0]
        
        self.heap[0] = self.heap[self.count - 1]
        del self.heap[self.count - 1]
        self.count -= 1
        self.reverseHeapify(0)
        return root
        
    def reverseHeapify(self, index):
        """ This does the opposite of heapify, it starts at a parent, and 
        recursively swaps it with children that are smaller , in order to
        maintain a valid heap"""

        RchildIndex = self.rightChild(index)
        LchildIndex = self.leftChild(index)
        
        """First, checks if parent has either left or right children, gets them if so """
        if RchildIndex != -1:
            Rchild = self.heap[RchildIndex]
        else:
            Rchild = 0

        if LchildIndex != -1:
            Lchild = self.heap[LchildIndex]
        else:
            Lchild = 0
        
        curr = self.heap[index]
        
        """ Compares to decide which child the parent should be swapped with """
        if Lchild and Rchild:
            if min(Lchild, Rchild) == Lchild:
                swapWithIndex = LchildIndex
                swapData = Lchild
            else:
                swapWithIndex = RchildIndex
                swapData = Rchild
        elif Lchild:
            swapWithIndex = LchildIndex
            swapData = Lchild
        else:
            swapWithIndex = RchildIndex
            swapData = Rchild

        if swapData < curr:
            self.swap(swapWithIndex, index)
            self.reverseHeapify(swapWithIndex)
    
    
    def parent(self, index):
        """Gets parent index of a specified indexi, returns -1 if root"""
        if index != 0:
            return int((index - 2) / 2)
        else:
            return -1

    def rightChild(self, index):
        """Gets right child index of specified index"""
        index = int((index * 2) + 1)
        if index >= self.count:
            return -1
        else:
            return index

    def leftChild(self, index):
        """Gets left child index of specified index"""
        index = int((index * 2) + 2)
        if index >= self.count:
            return -1
        else:
            return index

    def swap(self, greater, lower):
        """Swaps the data stored at index greater with the data stored at 
        index lower, in the  heap"""
        temp = self.heap[greater]
        self.heap[greater] = self.heap[lower]
        self.heap[lower] = temp
    
    def size(self):
        return self.count

    def __str__(self):
        string = "Size: " + str(self.count) + "\nIndex\t\tValue\n"
        ind = 0
        for thing in self.heap:
            string += str(ind) + "\t\t" + str(thing) + "\n"
            ind += 1
        string += "\n"
        return string



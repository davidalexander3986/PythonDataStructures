"""Here is my implementation of a priority queue, using the minheap I made 
(minheap.py) as the backend """

import minheap

class PriorityQueue:

    def __init__(self):
        self.heap = minheap.minHeap()
        

    def push(self, data):
        self.heap.add(data)
    
    def pop(self):
        return self.heap.removeMin()

    def peek(self):
        return self.heap.getMin()

    def size(self):
        return self.heap.size()

    def __str__(self):
        return str(self.heap)
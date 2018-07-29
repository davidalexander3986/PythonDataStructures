
""" This is the class for a single Node, which will be used in my Ternary Search 
Trie (TST) implementation """

class Node:

    def __init__(self):
        self.key = None
        self.right = None
        self.left = None
        self.middle = None
        self.isWord = False
        self.word = None

    def addRight(self, word):
        self.right = Node()
        self.right.key = word[0]

    def addLeft(self, word):
        self.left = Node()
        self.left.key = word[0]
    
    def addMiddle(self, word):
        self.middle = Node()
        self.middle.key = word[0]
   
    def extend(self, word, origWord):
    
        if word[0] == self.key:
            self.addMiddle(word)
            nextNode = self.middle
        elif word[0] > self.key:
            self.addRight(word)
            nextNode = self.right
        elif word[0] < self.key:
            self.addLeft(word)
            nextNode = self.left
        if len(word) > 1:
            nextNode.extend(word[1:], origWord)
        else:
            print(origWord)
            self.setEnd(origWord)


    def getWord(self):
        if self.isWord:
            return self.word
        else:
            return None

    def hasRight(self):
        if self.right != None:
            return True
        else:
            return False
    
    def hasLeft(self):
        if self.left != None:
            return True
        else:
            return False

    def hasMiddle(self):
        if self.middle != None:
            return True
        else:
            return False




    def setEnd(self, word):
        self.isWord = True
        self.word = word


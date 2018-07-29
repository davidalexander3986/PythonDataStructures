""" This is my implementation for a ternary search trie. In my second year 
of college, I had to implement a multi-way trie to build an autocomplete
function, so it seemed fitting that I implment a ternary trie this time, 
in a step forward in my mission to become advanced in Python"""

import TrieNode as TN
class Trie:

    def __init__(self):
        self.head = None
        self.wordCount = 0

    def insert(self, word):
        if self.head == None:
            self.head = TN.Node()
            self.head.key = word[0]
            self.head.extend(word[1:], word)
        else:
            self.head.extend(word, word)
    
    def lookup(self, word):
        curr = self.head
        wordCopy = word
        if self.head == None:
            return False
        while len(word) > 0:
            print(curr.getWord())
            if wordCopy == curr.getWord():
                return True
            else:
                if word[0] == curr.key:
                    if curr.hasMiddle():
                        curr = curr.middle
                        word = word[1:]
                    else:
                        return False
                elif word[0] > curr.key:
                    if curr.hasRight():
                        curr = curr.right
                        word = word[1:]
                    else:
                        return False
                elif word[0] < curr.key:
                    if curr.hasLeft():
                        curr = curr.left
                        word = word[1:]
                    else:
                        return False
        return True



       

        


                

                    


                

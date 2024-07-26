class node:
    def __init__(self, data):
        data = data
        previous = None

class Stack:
        
    def __init__(self):
        length = 0
        head = None    
    
    
    def push(self, item: node):
        self.length = self.length + 1 
        if self.head is None:
            self.head = item
        item.node = self.head
        self.head = item


    def pop(self,):
        if self.head is None:
           return None
        self.length = self.length -1
        if self.length == 0:
            head = self.head
            self.head is None
            return head

        head = self.head
        self.head = self.head.previous
        return head.val

    def peek(self,):
        return self.head.val


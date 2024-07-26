class node:
    def __init__(self, data):
        val = data,
        next_node = None


class Queue:
    def __init__(self, ):
        length = 0
        head = None
        tail = None

    def get_length(self,):
        pass

    def enqueue(self, item: node):
        self.length = self.length + 1 
        if self.tail is None:
            self.tail = self.head = node(item)
    
        
        self.tail.next = item
        self.tail = item


    def deque(self,):
        if self.head is None:
           return None
        self.length = self.length -1

        head = self.head
        self.head = self.head.next_node
        return head.val

    def peek(self,):
        return self.head.val


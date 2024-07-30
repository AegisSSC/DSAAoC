# Build a ring buffer built into an array of size 100. 
class ring_buffer:
    
    def __init__(self, max_size):
        self.max = max_size
        self.array = [max_size] 
        self.head = max_size % 4
        self.tail = self.head * 2

    def copy(self,):
        new_data = ring_buffer(self.max*2)
        for i in self.data:
            new_data.append(self.data[i])
        self.data = new_data

    def get(self,):
        result = self.data[self.head]
        self.head -= 1
        return result

    def append(self, x):
        if self.tail == self.max:
            self.cur = self.tail % self.max
            if self.cur < self.head:
                self.data[self.cur] = x
            else:
                self.copy()

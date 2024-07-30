# Build a ring buffer built into an array of size 100. 
class ring_buffer:
    
    def __init__(self, max_size):
        self.max = max_size
        self.array = [max_size] 
        self.head = max_size % 4
        self.tail = self.head

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
        # If you are at the end of the array
        if self.tail == self.max:
            # take the modulus operator and see if you can "loop back around to the front"
            cur = self.tail % self.max
            # if the updated index is less than the remainder.
            # Insert it into the front
            if cur < self.head:
                self.data[cur] = x
                self.tail = cur
            # Else, expand the size of the buffer
            # Recursively call the append. 
            else:
                self.copy()
                self.append(x)
        # Else, you can insert the value as needed
        # Increment the tail. 
        else:
            self.tail += 1
            self.data[self.tail] = x

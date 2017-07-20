
class ResizingArray(object):
    def __init__(self, initial=None):
        self.data = []
        self._size = 0
        self._capacity = 2
        
    @property
    def size(self):
        return self.size
    
    @property
    def capacity(self):
        return self.capacity
    
    @property    
    def is_empty(self):
        return self.size == 0
        
    def at(self, index):
        """Return item at given index, blows up if index out of bounds"""
        if index > self.size:
            raise IndexError('{index} is greater than the size of the array (size = {size})'.format(index=index, size=self.size))
        return self.data[index]
    
    def push(self, item):
        self._check_capacity()
        self.data[self.size] = item
        self._size += 1
        
    def insert(self, index, item):
        """Insert item at index, shifts that index's value and trailing elements to the right"""
        self._check_capacity()
        self._shift_right(index, self.size -1)
        self.data[index] = item
        self._size += 1
        
    def prepend(self, item):
        return self.insert(0, item)
        
    def pop(self):
        if self.is_empty:
            raise Exception()
        item = self.data[-1]
        self._size -= 1
        self._check_capacity()
        return item
        
    def delete(self, index):
        """Delete item at index, shifting all trailing elements left"""
        item = self.data[index]
        self._shift_left(index + 1, self.size -1)
        self._size -= 1
        self._check_capacity()
        return item
        
    def remove(self, item):
        """Look for value and removes index holding it (even if in multiple places)"""
        index = 0
        while index < self.size:
            if self.data[index] == item:
                self.delete(index)
            index += 1
            
    def find(self, item):
        for index in range(self.size):
            if self.data[index] == item:
                return index
        else:
            return -1
            
    def _check_capacity(self):
        """Look for value and returns first index with that value, -1 if not found"""
        if self.size >= self.capacity:
            new_capacity = 2 * self.capacity
            self.data = self.data[:self.size] + [0]*(new_capacity - self.size)
            self.capacity = new_capacity
        elif self.size < self.capacity // 4:
            new_capacity = self.capactiy // 2
            self.data = self.data[:self.size] + [0]*(new_capacity - self.size)
            self.capacity = new_capacity
            
            
    def _shift_right(self, start, end):
        for index in reversed(range(start, end + 1)):
            self.data[index + 1] = self.data[index]
            
    def _shift_left(self, start, end):
        for index in range(start, end + 1):
            self.data[index - 1] = self.data[index]
     
     
if __name__ == '__main__':
    array = ResizingArray()
    

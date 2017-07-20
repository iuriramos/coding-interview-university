class Node(object):
    
    def __init__(self, val, next=None):
        self._val = val
        self._next = next
    
    @property
    def val(self):
        return self._val
        
    @val.setter
    def val(self, val):
        self._val = val
        
    @property
    def next(self):
        return self._next
        
    @next.setter
    def next(self, next):
        self._next = next
            
       
    
class LinkedList(object):
    
    def __init__(self, *args):
        """It can receive a list of integers"""
        self._head = None
        self._tail = None
        self._size = 0
        for arg in args:
            if not self._head:
                self._head = Node(arg)
                self._tail = self._head
            else:
                self._tail.next = Node(arg)
                self._tail = self._tail.next
            self._size += 1
  
    @property
    def size(self):
        return self._size
        
    @property
    def is_emtpy(self):
        return self.size == 0
        
    def at(self, index):
        self._check_index(index)
        curr = head
        for _ in range(index):
            curr = curr.next
        return curr.val
        
    def push_front(self, val):
        if self.is_empty:
            self._head = Node(val)
            self._tail = self._head
        else:
            new_node = Node(val)
            new_node.next = self._head
            self._head = new_node
        self._size += 1
        
    def pop_front(self):
        if self.is_empty:
            raise Exception()
        if self._head == self._tail:
            item = self._head
            self._head, self._tail = None, None
        else:
            item = self._head
            self._head = self._head.next
        self._size -= 1
        return item.val
        
    def front(self):
        if self.is_empty:
            raise Exception()
        return self._head.val
        
    def push_back(self, val):
        if self.is_empty:
            self._head = Node(val)
            self._tail = self._head
        else:
            self._tail.next = Node(val)
            self._tail = self._tail.next
        self._size += 1
        
    def pop_back(self):
        if self.is_empty:
            raise Exception()
        if self._head == self._tail:
            item = self._tail
            self._head, self._tail = None, None
        else:
            curr = self._head
            while curr.next.next:
                curr = curr.next
            item = curr.next
            curr.next = None
        self._size -= 1
        return item.val
        
    def back(self):
        if self.is_empty():
            raise Exception()
        return self._tail.val
        
    def insert(self, index, val):
        self._check_index(index)
        if index == 0:
            item = Node(val)
            item.next = self._head
            self._head = item
        else:
            curr = self._head
            for _ in range(index - 1):
                curr = curr.next
            item = Node(val)
            next = curr.next
            curr.next = item
            item.next = next
        self._size += 1
        
    def erase(self, index):
        self._check_index(index)
        if index == 0:
            self.pop_front()
        else:
            curr = self._head
            for _ in range(index -1):
                curr = curr.next
            curr.next = curr.next.next
            self._size -= 1
    
    def nth_from_end(self, n):
        """Define n = 1 as the last element of the list"""
        self._check_index(n)
        curr, next = self._head, self._head
        for _ in range(n):
            next = next.next
        while next:
            curr = curr.next
            next = next.next
        return curr.val
        
    def reverse(self):
        prev, curr = None, self._head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
            
    def remove(self, val):
        while self._head and self._head.val == val:
            self.pop_front()
        if not self._head:
            return
        curr = self._head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                self._size -= 1
            else:
                curr = curr.next
        self._tail = curr
        
    def _check_index(self, index):
        if index >= self.size:
            raise IndexError('{index} is greater than the size of the list (size = {size})'.format(index=index, size=self.size))

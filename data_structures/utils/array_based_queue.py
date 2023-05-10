
class ArrayQueue:
    def __init__(self,c = 4):
        self._data = [None] * c
        self._size = 0
        self._front = 0
        self._capacity = c
        
    def __len__(self):
        return self.get_size()
    
    def is_empty(self):
        return self.get_size() == 0
    
    def enqueue(self,val):
        
        if self.get_size() == self.get_capacity():
            self._resize(2 * self.get_capacity())
        
        avail = (self.get_front() + self.get_size()) % len(self._data)
        self._data[avail] = val
        self._set_size(self.get_size() + 1)
        
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        if self.get_size() < self.get_capacity() // 4:
            self._resize(self.get_capacity() // 2)
        val = self._data[self._front]
        self._data[self._front] = None # Help garbage collector
        self._set_front((self.get_front() + 1) % len(self._data))
        self._set_size(self.get_size() - 1)
        return val
    
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self._data[self._front % len(self._data)]
    
    def _resize(self,new_capacity):
        new_arr = [None] * new_capacity
        front = self.get_front()
        for i in range(self.get_size()):
            new_arr[i] = self._data[front]
            front = (front + 1) % len(self._data)
        self._data = new_arr
        self._set_capacity(new_capacity)
        self._set_front(0)

    
    def get_size(self):
        return self._size
    
    def _set_size(self,size):
        self._size = size
        
    def get_front(self):
        return self._front
    
    def _set_front(self,front):
        self._front = front
        
    def get_capacity(self):
        return self._capacity
    
    def _set_capacity(self,capacity):
        self._capacity = capacity
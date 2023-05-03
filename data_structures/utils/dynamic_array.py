class DynamicArray:
    def __init__(self , capacity = 1):
        self._size = 0
        self._capacity = capacity
        self.arr = self._make_array(self.get_capacity())
    
    def is_empty(self):
        return self.get_size() == 0
    
    def at(self, index):
        if index >= self.get_size():
            return "Index out of bounds"
        return self.arr[index]
    
    def push_back(self,val):
        if self.get_size() == self.get_capacity():
            self._resize(2 * self.get_capacity())
        self.arr[self.get_size()] = val
        self._set_size(self.get_size() + 1)
    
    def pop_back(self):
        if self.is_empty():
            return "Array is empty"
        
        if self.get_size() < self.get_capacity() // 4:
            self._resize(self.get_capacity() // 2)
        
        val = self.arr[self.get_size() - 1]
        # del self.arr[self.get_size() - 1]
        self._set_size(self.get_size() - 1)
        return val
    
    def insert(self,index,val):
        if self.get_size() == self._capacity:
            self._resize(2 * self._capacity)
        self._move_forward(index)
        self.arr[index] = val
        self._set_size(self.get_size() + 1)
        
    def delete(self,index):
        if self.is_empty():
            return "Array is empty"
        
        if self.get_size() < self.get_capacity() // 2:
            self._resize(self.get_capacity() // 2)
        
        val = self.arr[index]
        self._move_backward(index)
        self._set_size(self.get_size() - 1)
        return val
    
    def remove(self,item):
        for i in range(self.get_size()):
            if self.arr[i] == item:
                self.delete(i)
    
    def find(self,item):
        for i in range(self.get_size()):
            if self.arr[i] == item:
                return i
        return -1
    
    def _move_forward(self, index):
        for i in range(self.get_size(), index, -1):
            self.arr[i] = self.arr[i - 1]
            
            
    def _move_backward(self, index):
        for i in range(index, self.get_size()):
            self.arr[i] = self.arr[i + 1]

    def _resize(self, new_capacity):
        print("Resizing from {} to {}".format(self.get_capacity(), new_capacity))
        
        new_arr = self._make_array(new_capacity)
        for i in range(self.get_size()):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self._set_capacity(new_capacity)
    
    def _make_array(self, capacity):
        return [0] * capacity
    

    
    
    def get_capacity(self):
        return self._capacity
    
    def _set_capacity(self, capacity):
        self._capacity = capacity
    
    def get_size(self):
        return self._size
    
    def _set_size(self, size):
        self._size = size
    
    def get_arr(self):
        return self.arr
    

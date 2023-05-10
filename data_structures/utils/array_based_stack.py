from utils.dynamic_array import DynamicArray

class ArrayStack:
    def __init__(self):
        self._data = DynamicArray()
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self,val):
        self._data.push_back(val)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self._data.pop_back()
    
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self._data.at(self._data.get_size() - 1)
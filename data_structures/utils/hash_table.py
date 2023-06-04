from collections.abc import MutableMapping
from typing import Iterator
from utils.linked_list import SinglyLinkedList

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class."""
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __eq__(self, other):
            try:
                return self._key == other._key
            except :
                return False
        def __ne__(self, other):
            try:
                return self._key != other._key
            except :
                return True
        def __lt__(self, other):
            return self._key < other._key 


# this is the implementation of the map ADT using a python list
# this is a very inefficient implementation, but it is a good starting point
class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""
    def __init__(self):
        """Create an empty map."""
        self._table = [] 

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value 
        raise KeyError('Key Error: ' + repr(k)) 

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key: # Found a match:
                item._value = v # reassign value
                return # and quit
        # did not find match for key
        self._table.append(self._Item(k,v)) 

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key: # Found a match:
                self._table.pop(j) # remove item
                return # and quit
        raise KeyError('Key Error: ' + repr(k)) 

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table) 

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key # yield the KEY


class ChainingHashTable(MapBase):
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 4
        self._table = [None] * self._capacity
        
    def _hash_function(self, k):
        return hash(k) % self._capacity
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def __setitem__(self, key, value) -> None:
        k = self[key]
        if k != 'Key Error: ' + repr(key):
            del self[key]
        
        
        if self._size > (self._capacity // 3) * 2:
            self._resize(self._capacity * 2)
        j = self._hash_function(key)
        if self._table[j] is None:
            self._table[j] = SinglyLinkedList()
        self._table[j].push_back(self._Item(key, value))
        self._size += 1
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            return ('Key Error: ' + repr(k))
        for item in bucket:

            if k == item._key:
                
                return item._value
        return ('Key Error: ' + repr(k))
    
    def __delitem__(self, k):
        if self._size < self._capacity // 3:
            self._resize(self._capacity // 2)
        
        j = self._hash_function(k)
        bucket = self._table[j]
        if bucket is None:
            return ('Key Error: ' + repr(k))
        
        pos = 0
        for item in bucket:
            if k == item._key:
                bucket.erase(pos)
                self._size -= 1
                return
            pos += 1
            
        return ('Key Error: ' + repr(k))

    def __iter__(self) -> Iterator:
        for bucket in self._table:
            if bucket is not None:
                for item in bucket:
                    yield item._key
    
    def _resize(self, c):
        old = self._table
        self._table = [None] * c
        self._size = 0
        self._capacity = c
        for bucket in old:
            if bucket is not None:
                for item in bucket:
                    self[item._key] = item._value


class LinearProbingHashTable(MapBase):
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 4
        self._table = [None] * self._capacity
        
    def _hash_function(self, k):
        return hash(k) % self._capacity
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def __setitem__(self, key, value) -> None:
        
        if self._size > (self._capacity // 3) * 2:
            self._resize(self._capacity * 2)
        j = self._hash_function(key)
        
        while self._table[j] is not None and self._table[j]._key != key:
            j = (j + 1) % self._capacity
        if self._table[j] is None:
            self._size += 1
        self._table[j] = self._Item(key, value)

    def __getitem__(self, k):
        j = self._hash_function(k)
        while self._table[j] is not None:
            if self._table[j]._key != 'DELETED' and k == self._table[j]._key:
                return self._table[j]._value
            
            j = (j + 1) % self._capacity
        return ('Key Error: ' + repr(k))
    
    def __delitem__(self, k):
        if self._size < self._capacity // 3:
            self._resize(min((self._capacity // 2) +1 , 4))
        
        j = self._hash_function(k)
        while self._table[j] is not None:
            if k == self._table[j]._key:
                self._table[j] = self._Item('DELETED', None)
                self._size -= 1
                return
            j = (j + 1) % self._capacity
            
        return ('Key Error: ' + repr(k))

    def __iter__(self) -> Iterator:
        for item in self._table:
            if item is not None:
                yield item._key
    
    def _resize(self, c):
        old = self._table
        self._table = [None] * c
        self._capacity = c
        self._size = 0
        for item in old:
            if item is not None and item._key != 'DELETED':
                self[item._key] = item._value


class QuadraticProbingHashTable(LinearProbingHashTable):
    def __init__(self) -> None:
        super().__init__()
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        i = 1
        while self._table[j] is not None :
            if k == self._table[j]._key:
                return self._table[j]._value
            j = (j + i**2) % self._capacity
            i += 1
        return ('Key Error: ' + repr(k))
    
    def __setitem__(self, key, value) -> None:        
        if self._size > (self._capacity // 3) * 2:
            self._resize(self._capacity * 2)
        j = self._hash_function(key)
        i = 1
        cnt =10
        while self._table[j] is not None and self._table[j]._key != key:
            if cnt:
                cnt -= 1
            j = (j + i**2) % self._capacity
            i += 1
        if self._table[j] is None:
            self._size += 1
        self._table[j] = self._Item(key, value)
        
    def __delitem__(self, k):
        if self._size < self._capacity // 3:
            self._resize(min((self._capacity // 2) +1 , 4))
        
        j = self._hash_function(k)
        i = 1
        while self._table[j] is not None:
            if k == self._table[j]._key:
                self._table[j] = self._Item('DELETED', None)
                self._size -= 1
                return
            j = (j + i**2) % self._capacity
            i += 1
            
        return ('Key Error: ' + repr(k))


class DoubleHashingHashTable(LinearProbingHashTable):
    def __init__(self) -> None:
        super().__init__()

    def _hash_function2(self, k):
        return 1
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        i = 1
        while self._table[j] is not None :
            if self._table[j]._key != 'DELETED' and k == self._table[j]._key:
                return self._table[j]._value
            j = (j + self._hash_function2(k)) % self._capacity
            i += 1
        return ('Key Error: ' + repr(k))

    def __setitem__(self, key, value) -> None:        
        if self._size > (self._capacity // 3) * 2:
            self._resize(self._capacity * 2)
        j = self._hash_function(key)
        i = 1
        while self._table[j] is not None and self._table[j]._key != key:
            j = (j + self._hash_function2(key)) % self._capacity
            i += 1
        if self._table[j] is None:
            self._size += 1
        self._table[j] = self._Item(key, value)


    def __delitem__(self, k):
        if self._size < self._capacity // 3:
            self._resize(min((self._capacity // 2) +1 , 4))
        
        j = self._hash_function(k)
        i = 1
        while self._table[j] is not None:
            if k == self._table[j]._key:
                self._table[j] = self._Item('DELETED', None)
                self._size -= 1
                return
            j = (j + self._hash_function2(k)) % self._capacity
            i += 1
            
        return ('Key Error: ' + repr(k))
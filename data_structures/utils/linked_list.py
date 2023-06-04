"""
All the data structures in this file are implemented using the Linked List data structure.
or related to the Linked List data structure.
"""

class Node:
        __slots__ = '_element', '_next'

        def __init__(self,element = None, next = None) -> None:
            """Node of a singly linked list."""
            self._element = element
            self._next = next


class DoublyNode(Node):
    __slots__ = '_prev'
    def __init__ (self, element, prev, next):
        super().__init__(element, next)
        self._prev = prev


class SinglyLinkedList:

    def __init__(self) -> None:
        """Create an empty linked list."""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self) -> int:
        """Return the number of elements in the linked list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return True if the linked list is empty."""
        return self._size == 0
    
    def push_front(self, e) -> None:
        """Add element e to the front of the linked list."""
        self._head = Node(e, self._head)
        self._size += 1
    
    def pop_front(self) -> Node._element:
        """Remove and return the element from the front of the linked list."""
        if self.is_empty():
            return 'Linked list is empty'
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element
    
    def push_back(self, e) -> None:
        """Add element e to the back of the linked list."""
        newest = Node(e)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def pop_back(self) -> Node._element:
        """Remove and return the element from the back of the linked list."""
        ptr = self._head
        while ptr._next != self._tail:
            ptr = ptr._next
        element = self._tail._element
        
        self._tail = ptr
        self._tail._next = None
        self._size -= 1
        return element
    
    def front(self) -> Node._element:
        """Return (but do not remove) the element at the front of the linked list."""
        if self.is_empty():
            return 'Linked list is empty'
        return self._head._element
    
    def back(self) -> Node._element:
        """Return (but do not remove) the element at the back of the linked list."""
        if self.is_empty():
            return 'Linked list is empty'
        return self._tail._element
    
    def insert(self, e, position) -> None:
        """Add element e to the linked list at the given position."""
        if position == 0:
            self.push_front(e)
        elif position == self._size:
            self.push_back(e)
        else:
            newest = Node(e)
            ptr = self._head
            for _ in range(position-1):
                ptr = ptr._next
            newest._next = ptr._next
            ptr._next = newest
            self._size += 1
    
    def erase(self, position) -> Node._element:
        """Remove and return the element from the linked list at the given position."""
        if position == 0:
            return self.pop_front()
        elif position == self._size-1:
            return self.pop_back()
        else:
            ptr = self._head
            for _ in range(position-1):
                ptr = ptr._next
            element = ptr._next._element
            ptr._next = ptr._next._next
            self._size -= 1
            return element
    
    def value_n_from_end(self, n) -> Node._element:
        """Return the value of the element at nth position from the end of the linked list."""
        ptr = self._head
        for _ in range(self._size-n):
            ptr = ptr._next
        return ptr._element
    
    def reverse(self) -> None:
        """Reverse the linked list in-place."""
        ptr = self._head
        prev = None
        while ptr:
            next = ptr._next
            ptr._next = prev
            prev = ptr
            ptr = next
        self._head = prev
    
    def remove_value(self, value) -> None:
        """Remove the first item in the linked list with the given value."""
        ptr = self._head
        prev = None
        while ptr:
            if ptr._element == value:
                if prev:
                    prev._next = ptr._next
                else:
                    self._head = ptr._next
                self._size -= 1
                return
            prev = ptr
            ptr = ptr._next
        return 'Value not found'
    
    def value_at(self, position) -> Node._element:
        """Return the value of the element at the given position."""
        ptr = self._head
        for _ in range(position):
            ptr = ptr._next
        return ptr._element
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the linked list."""
        ptr = self._head
        while ptr:
            yield ptr._element
            ptr = ptr._next


class CircularLinkedList(SinglyLinkedList):

    def __init__(self) -> None:
        """Create an empty circular linked list."""
        super().__init__()
    
    def push_front(self, e) -> None:
        """Add element e to the front of the circular linked list."""
        newest = Node(e)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            self._tail._next = self._head
        else:
            newest._next = self._head
            self._tail._next = newest
            self._head = newest
        self._size += 1
    
    def pop_front(self) -> Node._element:
        """Remove and return the element from the front of the circular linked list."""
        if self.is_empty():
            return 'Circular linked list is empty'
        element = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        return element
    
    def push_back(self, e) -> None:
        """Add element e to the back of the circular linked list."""
        newest = Node(e)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            self._tail._next = self._head
        else:
            newest._next = self._head
            self._tail._next = newest
            self._tail = newest
        self._size += 1
        
    def pop_back(self) -> Node._element:
        """Remove and return the element from the back of the circular linked list."""
        if self.is_empty():
            return 'Circular linked list is empty'
        element = self._tail._element
        ptr = self._head
        while ptr._next != self._tail:
            ptr = ptr._next
        ptr._next = self._head
        self._tail = ptr
        self._size -= 1
        return element

    def front(self) -> Node._element:
        """Return (but do not remove) the element at the front of the circular linked list."""
        if self.is_empty():
            return 'Circular linked list is empty'
        return self._head._element
    
    def head(self) -> Node:
        return self._head


class CircularQueue(CircularLinkedList):
    def __init__(self) -> None:
        """Create an empty circular queue."""
        super().__init__()
    
    def enqueue(self, e) -> None:
        """Add element e to the back of the circular queue."""
        self.push_back(e)
    
    def dequeue(self) -> Node._element:
        """Remove and return the element from the front of the circular queue."""
        return self.pop_front()
    
    def current(self) -> Node._element:
        """Return (but do not remove) the element at the front of the circular queue."""
        return self.front()
    
    def rotate(self) -> None:
        """Rotate the circular queue so that the front element is now at the back of the queue."""
        self._head = self._head._next


class DoublyLinkedBase:
    def __init__(self) -> None:
        """Create an empty doubly linked list."""
        self._header = DoublyNode(None, None, None)
        self._tailer = DoublyNode(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0
    
    def __len__(self) -> int:
        """Return the number of elements in the doubly linked list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return True if the doubly linked list is empty."""
        return self._size == 0
    
    def _insert_between(self, e: DoublyNode._element, predecessor: DoublyNode, successor: DoublyNode) -> DoublyNode:
        """Add element e between two existing nodes and return the new node."""
        newest = DoublyNode(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node: DoublyNode) -> DoublyNode._element:
        """Delete nonsentinel node from the doubly linked list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedStack:
    
    def __init__(self) -> None:
        """Create an empty stack."""
        self._head = None
        self._size = 0
        
    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e) -> None:
        """Add element e to the top of the stack."""
        self._head = Node(e, self._head)
        self._size += 1
        
    def top(self) -> Node._element:
        """Return (but do not remove) the element at the top of the stack."""
        if self.is_empty():
            return 'Stack is empty'
        return self._head._element
        
    def pop(self) -> Node._element:
        """Remove and return the element from the top of the stack."""
        if self.is_empty():
            return 'Stack is empty'
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    
    def __init__(self) -> None:
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self) -> Node._element:
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            return 'Queue is empty'
        return self._head._element
    
    def dequeue(self) -> Node._element:
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            return 'Queue is empty'
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element
    
    def enqueue(self, e) -> None:
        """Add an element to the back of queue."""
        newest = Node(e)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


class LinkedDeque(DoublyLinkedBase):
    
    def first(self) -> DoublyNode._element:
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            return 'Deque is empty'
        return self._header._next._element
    
    def last(self) -> DoublyNode._element:
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            return 'Deque is empty'
        return self._tailer._prev._element
    
    def insert_first(self, e: DoublyNode._element) -> None:
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e: DoublyNode._element) -> None:
        """Add an element to the back of the deque."""
        self._insert_between(e, self._tailer._prev, self._tailer)
    
    def delete_first(self) -> DoublyNode._element:
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            return 'Deque is empty'
        return self._delete_node(self._header._next)
    
    def delete_last(self) -> DoublyNode._element:
        """Remove and return the element from the back of the deque."""
        if self.is_empty():
            return 'Deque is empty'
        return self._delete_node(self._tailer._prev)


class PositionalList(DoublyLinkedBase):
    class Position:
        """An abstraction representing the location of a single element."""
        
        def __init__(self, container: DoublyLinkedBase, node: DoublyNode) -> None:
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
        
        def element(self) -> DoublyNode._element:
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other) -> bool:
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other) -> bool:
            """Return True if other does not represent the same location."""
            return not (self == other)
        
    def __init__(self) -> None:
        super().__init__()
        
        
    def _validate(self, p: Position) -> DoublyNode:
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node: DoublyNode) -> Position:
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._tailer:
            return None
        else:
            return self.Position(self, node)
        
    def first(self) -> Position:
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self) -> Position:
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._tailer._prev)
    
    def before(self, p: Position) -> Position:
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p: Position) -> Position:
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def _insert_between(self, e: DoublyNode._element, predecessor: DoublyNode, successor: DoublyNode) -> DoublyNode:
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e: DoublyNode._element) -> Position:
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e: DoublyNode._element) -> Position:
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._tailer._prev, self._tailer)
    
    def add_before(self, p: Position, e: DoublyNode._element) -> Position:
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p: Position, e: DoublyNode._element) -> Position:
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p: Position) -> DoublyNode._element:
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p: Position, e: DoublyNode._element) -> DoublyNode._element:
        """Replace the element at Position p with e.
        
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    
    def sort(self):
        if len(self) >1:
            maker = self.first()
            while maker != self.last():
                pivot = self.after(maker)
                value = pivot.element()
                if value > maker.element():
                    maker = pivot
                else:
                    walk = maker
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                    self.delete(pivot)
                    self.add_before(walk, value)
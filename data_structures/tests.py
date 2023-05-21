from pyfiglet import figlet_format
from utils.linked_list import ( LinkedQueue,
                                LinkedStack,
                                CircularQueue,
                                SinglyLinkedList,
                                CircularLinkedList,
                                PositionalList,
                                )
from utils.dynamic_array import DynamicArray
from utils.array_based_stack import ArrayStack
from utils.array_based_queue import ArrayQueue

    
def test_array():
    #  _____ _____ ____ _____   ______   ___   _    _    __  __ ___ ____       _    ____  ____      _ __   __
    # |_   _| ____/ ___|_   _| |  _ \ \ / / \ | |  / \  |  \/  |_ _/ ___|     / \  |  _ \|  _ \    / \\ \ / /
    #   | | |  _| \___ \ | |   | | | \ V /|  \| | / _ \ | |\/| || | |        / _ \ | |_) | |_) |  / _ \\ V / 
    #   | | | |___ ___) || |   | |_| || | | |\  |/ ___ \| |  | || | |___    / ___ \|  _ <|  _ <  / ___ \| |  
    #   |_| |_____|____/ |_|   |____/ |_| |_| \_/_/   \_\_|  |_|___\____|  /_/   \_\_| \_\_| \_\/_/   \_\_|  
    
    print(figlet_format('TEST DYNAMIC ARRAY'))
    
    
    
    arr = DynamicArray()

    # test push_back
    for i in range(10):
        arr.push_back(i)
        assert arr.is_empty() == False

    assert arr.get_size() == 10

    # test pop_back
    for i in range(10):
        arr.pop_back()
        
    assert arr.get_size() == 0
    assert arr.pop_back() == "Array is empty"

    # test insert'
    for i in range(10):
        arr.push_back(i)

    for i in range(3):
        arr.insert(1, i)
        assert arr.get_size() == 10+i+1
        assert arr.at(1) == i
        
    # test delete
    for i in range(3):
        arr.delete(1)
        
    # fill array with 0, 1, 2
    for i in range(10):
        arr.push_back(i%3)
        
    # test remove
    arr.remove(2)

    # test find
    assert arr.find(3) == 2
    print(figlet_format('TEST PASSED'))
    print("\n\n=================================================================================\n\n")


def test_stack():
    #  _____ _____ ____ _____   ____ _____  _    ____ _  __
    # |_   _| ____/ ___|_   _| / ___|_   _|/ \  / ___| |/ /
    #   | | |  _| \___ \ | |   \___ \ | | / _ \| |   | ' / 
    #   | | | |___ ___) || |    ___) || |/ ___ \ |___| . \ 
    #   |_| |_____|____/ |_|   |____/ |_/_/   \_\____|_|\_\
        
    print(figlet_format('TEST STACK'))
    array_stack = ArrayStack()
    linked_stack = LinkedStack()
    
    assert array_stack.is_empty() == True
    assert linked_stack.is_empty() == True
    assert array_stack.pop() == "Stack is empty"
    assert linked_stack.pop() == "Stack is empty"
    
    
    for i in "Hello World":
        array_stack.push(i)
        linked_stack.push(i)
    
    array_stack_tmp = []
    linked_stack_tmp = []
    
    for i in range(len(array_stack)):
        array_stack_tmp.append(array_stack.pop())
        linked_stack_tmp.append(linked_stack.pop())
    
    assert "".join(array_stack_tmp) == "dlroW olleH"
    assert "".join(linked_stack_tmp) == "dlroW olleH"
    
    for i in "{([":
        array_stack.push(i)
        linked_stack.push(i)
    
    opposites = {"{":"}","[":"]","(":")"}
    for i in "])}":
        if opposites[array_stack.top()] == i:
            array_stack.pop()
        if opposites[linked_stack.top()] == i:
            linked_stack.pop()
    assert array_stack.is_empty() == True
    assert linked_stack.is_empty() == True
    
    for i in "{([":
        array_stack.push(i)
        linked_stack.push(i)
    
    for i in ")]}":
        if array_stack.top() == i:
            array_stack.pop()
        if linked_stack.top() == i:
            linked_stack.pop()
            
    assert array_stack.is_empty() == False
    assert linked_stack.is_empty() == False
        
    print(figlet_format('TEST PASSED'))
    print("\n\n=================================================================================\n\n")


def test_queue():
    #  _____ _____ ____ _____    ___  _   _ _____ _   _ _____ 
    # |_   _| ____/ ___|_   _|  / _ \| | | | ____| | | | ____|
    #   | | |  _| \___ \ | |   | | | | | | |  _| | | | |  _|  
    #   | | | |___ ___) || |   | |_| | |_| | |___| |_| | |___ 
    #   |_| |_____|____/ |_|    \__\_\\___/|_____|\___/|_____|
    
    print(figlet_format('TEST QUEUE'))
    
    array_queue = ArrayQueue()
    linked_queue = LinkedQueue()
    assert array_queue.is_empty() == True
    assert linked_queue.is_empty() == True
    assert array_queue.dequeue() == "Queue is empty"
    assert linked_queue.dequeue() == "Queue is empty"
    
    for i in "Hello World":
        array_queue.enqueue(i)
        linked_queue.enqueue(i)
    
    for i in "Hello World":
        assert array_queue.dequeue() == i
        assert linked_queue.dequeue() == i
    for i in range(100):
        array_queue.enqueue(i)
        linked_queue.enqueue(i)
    
    assert array_queue.is_empty() == False
    assert linked_queue.is_empty() == False
    
    for i in range(100):
        assert array_queue.dequeue() == i
        assert linked_queue.dequeue() == i
        
    assert array_queue.is_empty() == True
    assert linked_queue.is_empty() == True
    
    # test circular queue
    circular_queue = CircularQueue()
    
    assert circular_queue.is_empty() == True
    
    for i in range(100):
        circular_queue.enqueue(i)
    
    assert circular_queue.is_empty() == False
    assert circular_queue.current() == 0
    
    for i in range(1000):
        assert circular_queue.current() == i%100
        circular_queue.rotate()
    
    for i in range(100):
        circular_queue.dequeue()
        
    assert circular_queue.is_empty() == True
    
    print(figlet_format('TEST PASSED'))
    print("\n\n=================================================================================\n\n")


def test_linked_list():
    #  _____ _____ ____ _____   _     ___ _   _ _  _______ ____    _     ___ ____ _____ 
    # |_   _| ____/ ___|_   _| | |   |_ _| \ | | |/ / ____|  _ \  | |   |_ _/ ___|_   _|
    #   | | |  _| \___ \ | |   | |    | ||  \| | ' /|  _| | | | | | |    | |\___ \ | |  
    #   | | | |___ ___) || |   | |___ | || |\  | . \| |___| |_| | | |___ | | ___) || |  
    #   |_| |_____|____/ |_|   |_____|___|_| \_|_|\_\_____|____/  |_____|___|____/ |_| 
    
    print(figlet_format('TEST LINKED LIST'))
    
    singly = SinglyLinkedList()
    positional = PositionalList()
    circular = CircularLinkedList()
    
    assert singly.is_empty() == True
    assert positional.is_empty() == True
    assert circular.is_empty() == True
    
    for i in range(10):
        singly.push_front(i)
        positional.add_first(i)
        circular.push_front(i)
    
    # test circular linked list
    assert circular.is_empty() == False
    cur = circular.head()
    for i in range(100):
        assert cur != None
        cur = cur._next
    
    # test singly list
    for i in range(10):
        assert singly.pop_front() == 9-i
        assert circular.pop_front() == 9-i
    
    positional = PositionalList()
    
    # test positional list
    for i in range(10):
        positional.add_first(i)
        positional.add_last(i)
        positional.add_before(positional.first(), i)
        positional.add_after(positional.last(), i)
    
    
    tmp = []
    for i in range(10):
        tmp.append(i)
        tmp.append(i)
        tmp.append(i)
        tmp.append(i)
    
    positional.sort()
    
    idx = 0
    for i in positional:
        assert i == tmp[idx]
        idx += 1
    
    print(figlet_format('TEST PASSED'))
    

def test_hash_table():
    #  _____ _____ ____ _____   _   _    _    ____  _   _   _____  _    ____  _     _____ 
    # |_   _| ____/ ___|_   _| | | | |  / \  / ___|| | | | |_   _|/ \  | __ )| |   | ____|
    #   | | |  _| \___ \ | |   | |_| | / _ \ \___ \| |_| |   | | / _ \ |  _ \| |   |  _|  
    #   | | | |___ ___) || |   |  _  |/ ___ \ ___) |  _  |   | |/ ___ \| |_) | |___| |___
    #   |_| |_____|____/ |_|   |_| |_/_/   \_\____/|_| |_|   |_/_/   \_\____/|_____|_____|
    
    print(figlet_format('TEST HASH TABLE'))
    



def test_binary_tree():
    #  _____ _____ ____ _____   ____ ___ _   _    _    ______   __  _____ ____  _____ _____ 
    # |_   _| ____/ ___|_   _| | __ )_ _| \ | |  / \  |  _ \ \ / / |_   _|  _ \| ____| ____|
    #   | | |  _| \___ \ | |   |  _ \| ||  \| | / _ \ | |_) \ V /    | | | |_) |  _| |  _|  
    #   | | | |___ ___) || |   | |_) | || |\  |/ ___ \|  _ < | |     | | |  _ <| |___| |___ 
    #   |_| |_____|____/ |_|   |____/___|_| \_/_/   \_\_| \_\|_|     |_| |_| \_\_____|_____|
    
    print(figlet_format('TEST BINARY TREE'))
    

if __name__ == '__main__':
    test_array()
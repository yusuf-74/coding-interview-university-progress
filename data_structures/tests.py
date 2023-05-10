from pyfiglet import figlet_format
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
    stack = ArrayStack()
    assert stack.is_empty() == True
    assert stack.pop() == "Stack is empty"
    
    for i in "Hello World":
        stack.push(i)
    
    tmp = []
    
    for i in range(len(stack)):
        tmp.append(stack.pop())
    
    assert "".join(tmp) == "dlroW olleH"
    
    for i in "{([":
        stack.push(i)
    
    opposites = {"{":"}","[":"]","(":")"}
    for i in "])}":
        if opposites[stack.top()] == i:
            stack.pop()
    assert stack.is_empty() == True
    
    for i in "{([":
        stack.push(i)
    
    for i in ")]}":
        if stack.top() == i:
            stack.pop()
    assert stack.is_empty() == False
        
    print(figlet_format('TEST PASSED'))
    print("\n\n=================================================================================\n\n")


def test_queue():
    #  _____ _____ ____ _____    ___  _   _ _____ _   _ _____ 
    # |_   _| ____/ ___|_   _|  / _ \| | | | ____| | | | ____|
    #   | | |  _| \___ \ | |   | | | | | | |  _| | | | |  _|  
    #   | | | |___ ___) || |   | |_| | |_| | |___| |_| | |___ 
    #   |_| |_____|____/ |_|    \__\_\\___/|_____|\___/|_____|
    print(figlet_format('TEST QUEUE'))
    
    queue = ArrayQueue()
    
    assert queue.is_empty() == True
    assert queue.dequeue() == "Queue is empty"
    
    for i in "Hello World":
        queue.enqueue(i)
    
    for i in "Hello World":
        assert queue.dequeue() == i
        
    for i in range(100):
        queue.enqueue(i)
    
    assert queue.is_empty() == False
    
    for i in range(100):
        assert queue.dequeue() == i
        
    assert queue.is_empty() == True
    
    print(figlet_format('TEST PASSED'))
    print("\n\n=================================================================================\n\n")


def test_linked_list():
    #  _____ _____ ____ _____   _     ___ _   _ _  _______ ____    _     ___ ____ _____ 
    # |_   _| ____/ ___|_   _| | |   |_ _| \ | | |/ / ____|  _ \  | |   |_ _/ ___|_   _|
    #   | | |  _| \___ \ | |   | |    | ||  \| | ' /|  _| | | | | | |    | |\___ \ | |  
    #   | | | |___ ___) || |   | |___ | || |\  | . \| |___| |_| | | |___ | | ___) || |  
    #   |_| |_____|____/ |_|   |_____|___|_| \_|_|\_\_____|____/  |_____|___|____/ |_| 
    print(figlet_format('TEST LINKED LIST'))
    


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
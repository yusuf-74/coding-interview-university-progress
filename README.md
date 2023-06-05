# Coding-Interview-University-Progress
I will log any progress in jwasham study plan repo here and I will add some notes for each topic.

# Table of Contents

- [1. Big-O Notation](#1-big-o-notation)
- [2. Arrays](#2-arrays)
    - [Static Array](#static-array)
    - [Dynamic Array](#dynamic-array)
      - [Dynamic Array Implementation](#dynamic-array-implementation) 
    - [Summary](#summary)
- [3. Stacks](#3-stacks)
    - [Main Functions Time Complexity](#main-functions-time-complexity)
    - [Real Life Examples](#real-life-examples)
    - [Implementation](#stack-implementation)
- [4. Queues](#4-queues)
    - [Main Functions Time Complexity](#main-functions-time-complexity-1)
    - [Real Life Examples](#real-life-examples-1)
    - [Implementation](#queue-implementation)
- [5. Linked Lists](#5-linked-lists)
    - [Quick Summary](#quick-summary)
    - [Arrays vs. Linked Lists](#arrays-vs-linked-lists)
    - [Types of Linked Lists](#types-of-linked-lists)
      - [Singly Linked Lists](#singly-linked-lists)
        - [Singly Linked Lists Implementation](#singly-linked-lists-implementation)
      - [Circular Linked Lists](#circular-linked-lists)
        - [Circular Linked Lists Implementation](#circular-linked-lists-implementation)
      - [Doubly Linked Lists](#doubly-linked-lists)
        - [Doubly Linked Lists Implementation](#doubly-linked-lists-implementation)
      - [Positional Lists](#positional-lists)
        - [Positional Lists Implementation](#positional-lists-implementation)
- [6. Hash tables (python's Dictionary)](#6-hash-tables-pythons-dictionary)
  - [Collision](#collision)
  - [How to solve collision?](#how-to-solve-collision)
    - [chaining vs open addressing](#chaining-vs-open-addressing)
      - [Hashing with chaining](#hashing-with-chaining)
        - [Chaining implementation](#chaining-implementation)
      - [Hasing with open addressing](#hasing-with-open-addressing)
        - [probing strategies](#probing-strategies)
          - [Linear probing](#linear-probing)
            - [mathematical proof of clustering](#mathematical-proof-of-clustering)
            - [Linear Probing implementation](#linear-probing-implementation)
          - [Quadratic probing](#quadratic-probing)
            - [Quadratic Implementation](#quadratic-implementation)
          - [Double hashing](#double-hashing)
            - [Double Hashing Implementation](#double-hashing-implementation)
  - [Hashing functions in theory](#hashing-functions-in-theory)
    - [Division method](#division-method)
    - [Multiplication method](#multiplication-method)
    - [Universal hashing](#universal-hashing)
  - [Key sharing in python dictionary](#key-sharing-in-python-dictionary)


<br/>
<br/>
<br/>



# 1. Big-O Notation

**what is ***Big-O Notation*** and what is ***Omega*** and ***Theta*** ?**

- **Big-O Notation** is a mathematical Notation used to describe the limiting behavior of a function when the argument tends towards a particular value or infinity. It is commonly used in computer science to describe the time complexity of algorithms. In this context, it provides an upper bound on the number of operations required by an algorithm as a function of the input size.

  - **Big-O Notation Mathematical exepression**

    O(g(n)) = { f(n): there exist positive constants c and n0
            such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n0 }

  - ***Big-O Notation Graph***
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/big0.png" style = "width:100%" alt = "Figure for Big-Oh Notation">

- **Omega Notation**, on the other hand, provides a lower bound on the running time of an algorithm. It is used to describe the best-case running time of an algorithm.

  - **Omega Notation Mathematical exepression**

    Ω(g(n)) = { f(n): there exist positive constants c and n0 
            such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n0 }

  - ***Omega Notation Graph***
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/omega.png" style = "width:100%" alt = "Figure for Big-Oh Notation">

- **Theta Notation** is used to describe the tight bound on the running time of an algorithm. It provides both an upper and a lower bound on the running time of an algorithm. In other words, if a function is Θ(g(n)), then it is both O(g(n)) and Ω(g(n)).
 
  - **Theta Notation Mathematical exepression**

    Θ(g(n)) = { f(n): there exist positive constants c1, c2 and n0
            such that 0 ≤ c1g(n) ≤ f(n) ≤ c2g(n) for all n ≥ n0 }

  - ***Theta Notation Graph***
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/theta.png" style = "width:100%" alt = "Figure for Big-Oh Notation">

- **Big-O Notation** measures the upper bound or worst-case scenario for the growth rate of a function. In the context of computer science and algorithm analysis, it is used to describe the maximum amount of time an algorithm takes to solve a problem as the input size grows.

- **Big-O Complexity Chart**

  <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg" style = "width:100%" alt = "Figure for Big-Oh Notation">

<br />
<br />
<br />

# 2. Arrays

### Static Array 

- **Static Array**: Contiguous area of memory consisting of equal-size elements indexed by contiguous integers.

  - **Read / Write Time Complexity** 
    - **Access**: O(1)
    - **Add/Remove (start / middle)**: O(n)  
    - **Add/Remove (end)**: O(1)

### Dynamic Array

- **Dynamic Array**: A dynamic array is an array with a big improvement: automatic resizing.

- **Problem**: Static arrays are fixed in size, meaning they're not able to expand or contract once they're created. This is a problem for two reasons:
    - 1. We might insert items and then run out of capacity.
    - 2. We might delete items and end up with lots of empty space at the end of the array.
 
> " *All problems in computer science can be solved by another level of indirection.*" 
> - David Wheeler

 - **Solution**: dynamic arrays (also known as resizable arrays) 
 - **Idea**: store pointer to a dynamically allocated array and replace it with a newly-allocated array as needed.

 - #### **Dynamic Array Implementation**

    - GOTO [Dynamic Array Implementation](./data_structures/utils/dynamic_array.py)
### Summary

- Unlike static arrays, dynamic arrays can be resized.
- Appending an item to a dynamic array is O(1) on average, but O(n) worst-case, because of the possibility of having to allocate a new array and copy over the old elements.
- Some space is wasted the capacity is always at least the length of the array, but usually, it's somewhere between length and length * 2.

</br>
</br>
</br>

# 3. Stacks

- A **Stack** is a collection of objects that are inserted and removed according to thelast-in, ﬁrst-out (LIFO) principle.
- #### **Main Functions Time Complexity**
  - **push**: O(1)
  - **pop**: O(1) 
  - **top**: O(1) 

- #### **Real Life Examples**
  - Internet Web browsers store the addresses of recently visited sites 
    in a **Stack**. Each time a user visits a new site, that site’s address is “pushed” onto the
    **Stack** of addresses. The browser then allows the user to “pop” back to previously
    visited sites using the “back” button.
  
  - Text editors usually provide an “undo” mechanism that cancels recent 
    editing operations and reverts to former states of a document. This undo operation can be accomplished by keeping
    text changes in a **Stack**.

- #### **Stack Implementation**
  I used **Dynamic Array** to implement **Array Based Stack**.

    - The **adapter design pattern** applies to any context where we effectively want to
    modify an existing class so that its methods match those of a related, but different,
    class or interface. 
    One general way to apply the adapter pattern is to deﬁne a new
    class in such a way that it contains an instance of the existing class as a hidden
    ﬁeld, and then to implement each method of the new class using methods of this
    hidden instance variable.

  - GOTO [Array Stack Implementation](./data_structures/utils/array_based_stack.py)
  - GOTO [Linked Stack Implementation](./data_structures/utils/linked_list.py#L6)

</br>
</br>
</br>

# 4. Queues

- A **Queue** is another fundamental data structure. It is a close “cousin” of the stack,
as a queue is a collection of objects that are inserted and removed according to the
ﬁrst-in, ﬁrst-out (FIFO) principle.

- #### **Main Functions Time Complexity**
  - **enqueue**: O(1)
  - **dequeue**: O(1) 
  - **front**: O(1)
  
- #### **Real Life Examples**
  - Supermarket checkout lines: People line up in a **queue** to pay for their groceries. The first person to enter 
    the **queue** is  the first to be served by the cashier, and subsequent customers are served in the order 
    they joined the **queue**.

  - Customer service call centers: When a customer calls a support line, their call is put in a **queue** until 
    a representative is available to take their call. The representative will then take 
    the calls in the order they were received.

  - Printers: When multiple documents are sent to a printer, they are placed in a **queue** and processed one at a time.
    The first document to be sent to the printer is the first one to be printed, and the subsequent documents are 
    printed in the order they were received.

- #### **Queue Implementation**
  I used **Python List** to implement **Array Based Queue**.
  
  - GOTO [Queue Implementation](./data_structures/utils/array_based_queue.py)


<br />
<br />
<br />

# 5. Linked Lists

## Quick Summary

- ### What is a Linked List?
  >Linked lists are a fundamental data structure in computer science that are used to 
  >store and manipulate collections of data. They were invented as a way to address some of the limitations of arrays, which are another commonly used data structure.

  Another way to think of a linked list :

  >A linked list, in contrast, relies on a more distributed
  >representation in  which a lightweight object, known as a node, is allocated for each 
  >element. Each node maintains a reference to its element and one or more references to
  >neighboring nodes in order to collectively represent the linear order of the sequence

  - Node implementation:
    ```python
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self,element = None, next = None) -> None:
            """Node of a singly linked list."""
            self._element = element
            self._next = next
    ```
    **Important Note:** \__slots\__ is a special attribute that is used by the Python interpreter to allocate memory for the fixed set of attributes that we have declared for each instance of the class. This can save a significant amount of memory for large collections of objects.

</br>

- ### What is the **MAJOR** Problem with Arrays? 
  One of the main drawbacks of arrays is that they have a fixed size, which means that they cannot easily be resized or modified once they are created. This can be problematic when dealing with collections of data that need to be modified frequently, or when the size of the collection is not known in advance.

- ### How Linked Lists Solve this Problem?
  Linked lists were invented as a way to overcome this limitation by providing a dynamic data structure that can be easily resized and modified. Linked lists also have the advantage of allowing for efficient insertion and deletion of elements anywhere in the list, whereas arrays require shifting all subsequent elements when an element is inserted or deleted in the middle of the array.

## Arrays vs. Linked Lists

### Arrays:

**Advantages**:

- **Constant-time access** to individual elements using an index.
- **Cache-friendly** for iterating through all elements in sequence. **VERY IMPORTANT**
- **Can be resized dynamically** in some programming languages, such as Python.


**Disadvantages**:

- The length of a dynamic array might be longer than the actual number of
  elements that it stores.
- Amortized bounds for operations may be unacceptable in real-time systems.
  
- Inserting or deleting elements in the middle of an array can be **slow & expensive**,
  as it requires shifting all subsequent elements.
- Fixed size in some programming languages, such as C, which requires allocating a new
  array and copying all elements to resize.
- Wasted space if the array is only partially filled, which can be an issue with large 
  arrays or in memory-constrained environments.


### Linked lists:

**Advantages**:

- **Efficient insertion and deletion** of elements anywhere in the list.
- **No wasted space**, as each element only requires as much memory as it needs.
- Can be used to **implement more complex data structures**, such as stacks and queues.


**Disadvantages**:

- **No constant-time access** to individual elements; accessing an element requires traversing the list from the beginning.
- Can have **poor cache performance** if elements are not stored sequentially in memory.
- **Not supported natively in some programming** languages, requiring manual implementation.


In summary, arrays are good for situations where random access to individual elements is important and iteration is straightforward, while linked lists are better for situations where efficient insertion and deletion of elements is important, and memory efficiency is a concern.

## Types of Linked Lists

### Singly Linked Lists

- **Singly Linked Lists**: in its simplest form, is a collection of nodes that 
  collectively form a linear sequence. Each node stores a reference to an object that 
  is an element of the sequence, as well as a reference to the next node of the list

  - **Singly Linked Lists**

    <img src="https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist_insert_at_start.png" style = "width:100%" alt = "Figure for Singly Linked Lists">

- #### Singly Linked Lists Implementation

  - GOTO [Singly Linked Lists Implementation](./data_structures/utils/linked_list.py#L23)

### Circular Linked Lists
- **Circular Linked Lists**: A circular linked list is a variation of a linked list in which the last element is linked to the first element. This forms a circular loop.
- it's quite useful in certain situations. For example, it can be used for round-robin scheduling, where the scheduler goes around a list of processes giving each of them a slice of time before going around the list again.

  - **Circular Linked Lists**

    <img src="https://media.geeksforgeeks.org/wp-content/uploads/CircularSinglyLinkedList.png" style = "width:100%" alt = "Figure for Circular Linked Lists">
- #### Circular Linked Lists Implementation
  - GOTO [Circular Linked Lists Implementation](./data_structures/utils/linked_list.py#L159)
### Doubly Linked Lists

- **Doubly Linked Lists**: A doubly linked list is a data structure that contains a sequence of nodes such that each node contains an object and references to the previous and next nodes in the list.
- >In order to avoid some special cases when operating near the boundaries of a doubly
  >linked list, it helps to add special nodes at both ends of the list: a header node at
  >the beginning of the list, and a trailer node at the end of the list. These “dummy”
  >nodes are known as sentinels (or guards), and they do not store elements of the
  >primary sequence.
  > - Data Structurs and Algorithms in Python, Goodrich, Tamassia & Goldwasser

  - **Doubly Linked List**

    <img src="https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/03/DLL1.png" style = "width:100%" alt = "Figure for Doubly Linked Lists">

- #### Doubly Linked Lists Implementation
  - GOTO [Doubly Linked Lists Implementation](./data_structures/utils/linked_list.py#L246) 


### Positional Lists

- **Positional Lists**: A positional list is an abstract data type that is similar to a list, except that the user can access and insert new elements at any position within the list, as opposed to just the back of the list. This allows for constant-time insertion and removal of elements at an arbitrary position within the list.

- **Why ?**
  >We wish to have a more general abstraction. For example,
  >although we motivated the FIFO semantics of a queue as a model for customers
  >who are waiting to speak with a customer service representative, or fans who are
  >waiting in line to buy tickets to a show, the queue ADT is too limiting. What if
  >a waiting customer decides to hang up before reaching the front of the customer
  >service queue? Or what if someone who is waiting in line to buy tickets allows a
  >friend to “cut” into line at that position? We would like to design an abstract data
  >type that provides a user a way to refer to elements anywhere in a sequence, and to
  >perform arbitrary insertions and deletions.
  > - Data Structurs and Algorithms in Python, Goodrich, Tamassia & Goldwasser

</br>

- #### Positional Lists Implementation
  - GOTO [Positional Lists Implementation](./data_structures/utils/linked_list.py#L399)


</br>
</br>


# 6. Hash tables (python's Dictionary)

**what is ***Hash tables*** ?**

- **Hash tables**: or **Maps** or **Dictionaries** are data structures that store key-value pairs
  - **Read / Write Time Complexity** 
    - **Lookup**: O(1) 
    - **Add/Remove (end)**: O(1)

- #### **Real Life Examples**
  - A university’s information system relies on some form of a student ID as a
    key that is mapped to that student’s associated record (such as the student’s
    name, address, and course grades) serving as the value.

  - The domain-name system (DNS) maps a host name, such as www.wiley.com,
    to an Internet-Protocol (IP) address, such as 208.215.179.146.
  - A social media site typically relies on a (nonnumeric) username as a key that
    can be efﬁciently mapped to a particular user’s associated information.
  - A computer graphics system may map a color name, such as turquoise ,
    to the triple of numbers that describes the color’s RGB (red-green-blue) rep-
    resentation, such as (64,224,208).
  - Python uses a dictionary to represent each namespace, mapping an identifying
    string, such as pi , to an associated object, such as 3.14159



> prehash really should not change </br>
> if you ever implemented **\_\_hash\_\_** for a class don't mess with it </br>
> make sure it's defined in such a way that it doesn't change over time</br>
> otherwise you'll have a bad time finding your objects in a dictionary</br>
> the **\_\_hash\_\_** function return the object ID by default</br>
> **For example**: List is not hashable because it's mutable and it does change over time</br>
> - MIT OPEN COURSEWARE

</br>

## Collision

**what is ***Collision*** ?**
>If there are two or more keys with the same hash value, then two different items
>will be mapped to the same bucket in A. In this case, we say that a collision has
>occurred. To be sure, there are ways of dealing with collisions, which we will
>discuss later, **but the best strategy is to try to avoid them in the ﬁrst place.**
> - Data Structures and Algorithms in Python (Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser)

</br>

## How to solve collision?


  - ## chaining vs open addressing

    - ### Hashing with chaining

        Hashing with chaining is a method of collision resolution
        In this method we use a linked list to store the collided keys
        </br>
        </br>
        <img src="https://www.eecs.umich.edu/courses/eecs380/ALG/niemann/s_fig31.gif" style ="width:100%" />
        </br>
        if we assume that n is the number of keys and m is the size of the table the average number of keys in each 
        linked list is n/m so the average time complexity of searching is O(1 + (n/m)) keep in mind that if the n is much
        smaller than m the average time complexity is O(1) but we will have a lot of empty space in the table
        and if the n is much bigger than m the average time complexity is O(n)
        </br>
        > so we want m to be big enough to avoid collision and small enough to avoid empty space
        > - MIT OPEN COURSEWARE
            
        #### so How to choose m?

        first approach is to choose m to be some small constant let's say 8 and we extend the table and shrink it when needed
        BUT thhis approach is comming with the previous concept of dynamic array **Amortization**</br>

        #### **Chaining implementation**:
        - GOTO [Chaining implementation](./data_structures/utils/hash_table.py#L69)


    - ### Hasing with open addressing

        in this method we use the next empty slot in the table to store the collided key</br>

    - #### **probing strategies**

        </br>

        1. ***Linear probing***

            in this method we use the next empty slot in the table to store the collided key according to the following formula
            </br>
            <code>
            h(key,i) = (h'(key) + i) mod m
            </code>
            where h'(key) is an ordinary hashing function</br>
            and i is the number of collisions</br>
            and m is the size of the table</br>
            and h(key,i) is the probing function</br>
            </br>
            - disadvantage of this method is **clustering**</br>

            > the problem with the clusters is that it will grow rapidly
            > for example if we have a table of size 100 and we have a cluster of 4 items in the table and we want to insert a new item
            > the probability of collision is 4/100 = 4% which is 4 time bigger than the probability of collision in the first place
            > and we can essentially argue through making probabilistic assumptions that that if in fact we use linear probing we will
            > lose our avg. constant time lookup
            > - MIT OPEN COURSEWARE
            
            </br>

            - #### **mathematical proof of clustering**


                consider the following </br>
                h'(key) is a perfect hashing function</br>
                alpha is the load factor "alpha = n/m"</br>
                <code>
                if : 0.01 <= alpha <= 0.99 </br>
                we will see clustering O(log(n)) size in our table </br>
                that means we will have O(log(n)) time complexity for lookup </br>
                </code>
                </br>
            
            - #### **Linear Probing implementation** 
              - GOTO [Linear Probing implementation](./data_structures/utils/hash_table.py#L146)

        1. ***Quadratic probing***
          
              in this method we use the next empty slot in the table to store the collided key according to the following formula</br>
              <code>
              h(key,i) = (i^2 + h'(key)) mod m
              </code>
              where h'(key) is an ordinary hashing function</br>
              and i is the number of collisions</br>
              and m is the size of the table</br>
              and h(key,i) is the probing function</br>
              </br>
              - disadvantage of this method is **primary clustering.**</br>
              </br> 
              
              - #### ***Quadratic Implementation***
                - GOTO [Quadratic Implementation](./data_structures/utils/hash_table.py#L211)  


        2. ***Double hashing***

            in this method we use the next empty slot in the table to store the collided key according to the following formula</br>
            <code>
            h(key,i) = (h'(key) + i*h''(key)) mod m
            </code>
            where h'(key) is an ordinary hashing function</br>
            and h''(key) is another hashing function</br>
            and i is the number of collisions</br>
            and m is the size of the table</br>

            - #### ***Double Hashing Implementation***
              - GOTO [Double Hashing Implementation](./data_structures/utils/hash_table.py#L257)


            </br>


        **Note:** that when we delete an item from the table we don't actually delete it</br>
        we just mark it as deleted so it doesn't affect the lookup</br>

    </br>
    </br>

## Hashing functions in theory
1. Division method
   
    in this method we divide the key by the size of the table and take the remainder</br>
    ```python
    def hash(key, size):
        return key % size
    ```
</br>

2. Multiplication method

   key = a*k mod 2^w >> (w-r)</br>
   in this method we multiply the key by a constant a and take the most significant bits</br>
   where a is a random number between 0 and 2^w</br>
   and r is the number of bits we want to take</br>
   and w is the number of bits in word in the machine</br>
   ```python
    def hash(key, size):
        a = random.randint(0, 2**w)
         return ((a*key) % 2**w) >> (w-r)
    ```
</br>

3. Universal hashing

    key = (a*k + b) mod p mod m</br>
    in this method we multiply the key by a constant a and add another constant b and take the remainder</br>
    where a and b are random numbers between 0 and p</br>
    p is a huge prime number (bigger than the size of key universe)</br>
    m is the size of the table</br>
    ```python
    def hash(key, size):
        p = "HUGE PRIME NUMBER"
        a = random.randint(0, p)
        b = random.randint(0, p)
        return ((a*key) + b) % p % size
    ```

    </br>

    this method is better than the previous methods because it's more random</br>
    and if the a,b randomization is done correctly it will be very hard to find a collision</br>
    the Pr of collision is 1/m</br>


### Key sharing in python dictionary

for two dictionaries that are the same size and have the same keys
the keys will be stored in the same order in the two dictionaries
so instead of storing the keys for each dictionary we store them once
this is called key sharing</br>

it's super efficient because we don't have to store the keys for each dictionary and you can
notice the difference in memory usage when you have a lot of dictionaries with the same keys like in **"OOP"**

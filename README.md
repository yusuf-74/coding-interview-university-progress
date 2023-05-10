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

  GOTO [Stack Implementation](./data_structures/utils/array_based_stack.py)
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







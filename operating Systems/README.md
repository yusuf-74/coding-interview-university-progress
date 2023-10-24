# Operating systems CS 377

in this Section i will be adding all the notes i take in class and the code i write for the CS 377 Course



# Table of Contents
1. [Introduction](#1-introduction)
2. [OS Structure and Services](#2-os-structure-and-services)


</br>

# 1. Introduction

   - ### What is an Operating System?

     - interface between user and architecture (hide architecture details)
     - implements virtual machine that hopefully makes the computer easier to program than raw hardware

   </br>
     

   - ### What is the most salient feature of an OS?

     - **Services** the OS provides standard services (the user interface) which the hardware implements
       - exampels: file system, network, security, etc.
     - **Coordination** the OS coordinates the use of the hardware among the various applications and users to achieve efficiency and fairness
       - examples: Concurrency, Memory protection, Networking, Security, etc.
     - **Goal** Design and implement a system that is easy to program and efficient to execute

   </br>

   - ### Why study Operating Systems?

     - **Abstraction**: How to give illusion of infinite resources?
     - **System Design**: How to make tradeoffs between:
       - performance and convenience
       - performance and simplicity
       - putting functionality in hardware or software
     - **Basic Understanding**: the OS provides the services that allow application programs to run at all
     - **System intersecting point**: OS is the point where hardware and software meet 

   </br>
     
   - ### Modern OS functionality

     - **Processes and Threads Management**
       - process: a program in execution
       - thread: a unit of execution within a process
     - **Concurrency**: doing multiple things simultaneously
       - multiple processes/threads running at the same time
     - **I/O Device Management**: let the cpu do other things while waiting for I/O
       - disk, network, keyboard, mouse, etc.
     - **Memory Management**: allocate memory to processes and handle data movement between memory and disk
     - **File Systems**: manage persistent storage
     - **Distributed Systems and Networks**: manage multiple computers working together
     
   </br>



<!-- make a comparison table for 2 items -->
   - ### OS Services <--> Hardware support

     | OS Services         | Hardware support                                                                          |
     | ------------------- | ----------------------------------------------------------------------------------------- |
     | **Protection**      | **Kernel/User Mode**, protected instructions base/limit registers, memory management unit |
     | **Interrupts**      | interrupt vector                                                                          |
     | **System calls**    | trap instruction                                                                          |
     | **I/O**             | Interrupts, Memory-mapping I/O                                                            |
     | **Scheduling**      | Timer, privileged instructions                                                            |
     | **Synchronization** | atomic instructions, privileged instructions                                              |
     | **Virtual Memory**  | Memory-mapping I/O, privileged instructions                                               |

</br>

   - ### Examples:</br>

     - #### **Interrupts Based Asynchronous I/O**

       - Device controller has its own small processor which executes asynchronously with the main CPU
       - Device puts an interrupt signal on the bus when it is finished
       - CPU takes an interrupt
       
         1. Save Critical CPU state (hardware state)
         2. disable interrupts
         3. Save state that the interrupt handler will modify (software state)
         4. Invoke interrupt handler using Interrupt Vector
         5. Restore saved state
         6. Enable interrupts
         7. Restore critical CPU state, and continue execution of interrupted program
         
     - #### **Timer & Atomic Instructions**

       - **Timer**: generate an interrupt after a specified period of time
         - used to prevent a single process from monopolizing the CPU
         - used to implement time sharing
       - **Atomic Instructions**: cannot be interrupted
         - used to implement synchronization primitives
         - used to implement critical sections
    
     - #### **Synchronization**
       - interrupts interfere with other processes 
       - OS must provide synchronization primitives to allow processes to coordinate their actions
       
       Architecture must provide a garantee that short sequences of instructions will be executed atomically</br>
       There are **Two** Solutions:</br>
       1. Architecture mechanism to disable interrupts before sequence and re-enable after sequence
       2. A special instruction that is guaranteed to be atomic
           - **Test-and-set** instruction
           - **Swap** instruction
           - **Compare-and-swap** instruction 

     - #### **Virtual Memory**
       - Virtual memory is a technique that allows the execution of a process that is not completely in memory
       - instead of swapping entire processes in and out of memory, only the parts that are needed are swapped
       - the OS must manage the movement of data between memory and disk
       - in order for pieces of a process to be located and loaded into memory without causing a disruption to the process, the hardware provides a translation lookaside buffer (TLB) that caches the virtual to physical address translation to speed up the lookup process

</br>

# 2. OS Structure and Services

What are we going to cover in this section?

   1. More on system calls and interrupts
   2. Four major OS structures
       1. **Monolithic**: all OS components are in the kernel
       2. **Layered**: OS is divided into layers
       3. **Microkernel**: OS is divided into a small kernel and user-level servers
       4. **Modular**: OS is composed of dynamically loadable modules

   - ### 2.1 System Calls

     - Programming interface to the services provided by the OS
     - Typically written in a high-level language (C or C++)
     - Mostly accessed by programs via a high-level Application Program Interface (API) rather than direct system call use
     - Three most common APIs are Win32 API for Windows, POSIX API for POSIX-based systems (including virtually all versions of UNIX, Linux, and Mac OS X), and Java API for the Java virtual machine (JVM)
     - Why use APIs rather than system calls?
       - APIs safer than system calls (APIs are wrappers around system calls that do error checking and other things)
       - APIs allows for easier debugging
       - APIs is usually simpler than system calls
       - APIs is usually more flexible than system calls (Compitibility)

     - Image of System Calls

       ![System Calls](https://padakuu.com/image/slide_21.jpg)

     - #### ***System calls implementations***
        - Typically, a number is associated with each system call
          - System call interface maintains a table indexed according to these numbers
        - System call interface invokes intended system call in OS kernel and returns status of the system call and any return values
        - The caller need know nothing about how the system call is implemented
          - Just needs to obey API and understand what OS will do as a result call
          - Most details of OS interface hidden from programmer by API
            - Managed by run-time support library (set of functions built into libraries included with compiler)
      - #### ***System calls passing parameters***
        - Parameters can be passed in registers
          - Number of parameters is limited
        - Parameters can be stored in a block, or table, in memory, and the address of the block passed as a parameter in a register 
          - Called a **system call descriptor** or **handle**
          - This approach taken by Linux and Solaris
        - Parameters can also be passed on the stack
          - Parameters placed, or pushed, onto the stack by the program and popped off the stack by the operating system
     - #### ***Examples of System calls in Windows & Unix***
       ![System Calls](https://slideplayer.com/slide/11896867/67/images/26/Examples+of+Windows+and+Unix+System+Calls.jpg)

   - ### 2.2 OS structures
     
     </br>

     1. **Monolithic**
         - All OS components are in the kernel
         - Advantages
           - Simple and fast
           - Easy to debug
         - Disadvantages
           - No protection between OS components
           - A bug in any component can crash the entire system
           - Adding new functionality is difficult
           - Adding new functionality requires recompilation of the entire kernel
         - example: Mac OS X, Windows 8
         - ![Monolithic](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter2/2_11_DOS_Structure.jpg)
     
     </br>
  
     2. **Layered**
         - OS is divided into layers
         - Advantages
           - Protection between layers
           - Adding new functionality is easier
           - Adding new functionality does not require recompilation of the entire kernel
         - Disadvantages
           - Performance overhead of passing through layers
           - Layers are not always well-defined
         - example: THE, THEOS
         - ![Layered](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter2/2_13_Laered_OS.jpg)
     
     </br>
       
     3. **Microkernel**
         - OS is divided into a small kernel and user-level servers
         - Advantages
           - better reliability, esasier extension and customization
           - mediocre performance (unfortunately)
         - Disadvantages
            - more complex design
            - very high overhead for system processes communication
         - first microkernel: was Hydra at CMU '70. current systems include Chorus (France), Mach (CMU)
         - ![Microkernel](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter2/2_14_microkernelArchitecture.jpg)
     
     </br>
  
     4. **Modular**
         - Most modern OSs are modular
           - Uses object-oriented techniques
           - Each core component is separate
           - Each talks to the others via well-defined interfaces
           - Each is a loadable module as needed within the kernel
         - Overall similar to layered approach but more flexible
         - ![Modular](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter2/2_15_Solaris_Modules.jpg)


# 3. Process Management

   - A process as the unit of execution
   - How are processes represented in the OS?
   - what are possible execution states of a process and how does the system transition between them?
   - how are processes created and destroyed?
   - how do processes communicate with each other? Is this efficient?

   - ### What is a process?

     - **process**: dynamic execution context of an executing program
     - Several processes may run the same program but each process has its own execution context
     - A process executes sequentially, one instruction at a time
     - process state consists of at least:
       - the code for running program
       - the static data for running program
       - space for the dynamic data (heap), the heap pointer (HP)
       - the program counter (PC), indicating the next instruction to execute
       - an execution stack for procedure calls and returns, the stack pointer (SP)
       - values of CPU registers
       - a set of OS resources (open files, etc.)
       - process execution state (running, ready, blocked, etc.)

   - ### Process Execution States

     - Execution state of a process is defined by the current activity of that process
       - new (process is being created)
       - running (instructions are being executed)
       - ready (process is waiting to be assigned to a processor)
       - waiting (process is waiting for some event to occur)
       - terminated (process has finished execution)
     - As the program executes, it moves from state to state, as a result of interrupts, system calls, and scheduling decisions


     - ![Process Execution States](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter3/3_02_ProcessState.jpg)

  - ### Process Data Structures

    - **Process Control Block (PCB)**: Os data structure to keep track of all processes 
      - The PCB tracks the execution state and location of each process
      - The OS allocates a PCB for each process and places it on a queue
      - The OS deallocates the PCB when the process terminates 
    - **The PCB contains**:
      - Process state
      - program number
      - Program counter
      - Stack pointer
      - General-purpose registers
      - Memory Management information
      - Username of owner
      - List of open files
      - Queue pointers
      - CPU scheduling information
      - I/O status information
  
  - ### State Queues

    - The OS maintains a separate queue for each state
    - Each queue contains the PCBs of all processes currently in that state
    - The OS maintains a ready queue for processes that are ready to execute
    - The OS maintains a blocked queue for processes that are waiting for some event to occur
    - The OS maintains a running queue for processes that are currently executing
      - Note: the running queue is a bounded by the number of processors
    - The OS maintains a new queue for processes that are being created
    - The OS maintains a terminated queue for processes that have finished executing
    - ![State Queues](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/images/Chapter3/3_05_Queues.jpg)

# Go to [OS Notes For all Sections](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/)
"""
Semaphore Module

This module provides two semaphore implementations: 
    1.  BinarySemaphore and CountingSemaphore. 
    2.  Semaphores are synchronization constructs used for managing access to resources, 
        ensuring that multiple threads can coordinate their actions.

Classes:
    BinarySemaphore: A binary semaphore can have values 0 (locked) or 1 (unlocked). It is used for simple synchronization.
    CountingSemaphore: A counting semaphore allows multiple threads to access a limited pool of resources simultaneously.

Methods (Common to Both):
    wait: Wait for the semaphore to become available. If the semaphore is not available, the method will block until it is.
    signal: Signal that the semaphore is available or release a resource.

Classes and Methods Usage:
    semaphore = BinarySemaphore()  # Initialize a binary semaphore
    semaphore.wait()  # Wait for the semaphore
    semaphore.signal()  # Signal that the semaphore is available

    semaphore = CountingSemaphore(3)  # Initialize a counting semaphore with an initial count of 3
    semaphore.wait()  # Wait for the semaphore
    semaphore.signal()  # Signal that the semaphore is available
"""

# Constants
BUSY = 0
FREE = 1


from abc import ABC, abstractmethod

class Semaphore(ABC):
    """
    Semaphore

    This class is an abstract base class for all semaphore implementations.

    Methods:
        wait: Wait for the semaphore to become available. If the semaphore is not available, the method will block until it is.
        signal: Signal that the semaphore is available or release a resource.

    Usage:
        semaphore = Semaphore()  # This will raise an error, because you cannot initialize a Semaphore directly
    """

    @abstractmethod
    def wait(self):
        """
        Wait for the semaphore to become available.
        If the semaphore is not available, the method will block until it is.
        """
        pass

    @abstractmethod
    def signal(self):
        """
        Signal that the semaphore is available or release a resource.
        """
        pass

class BinarySemaphore(Semaphore):
    """
    Binary Semaphore

    This class implements a binary semaphore, which can have values 0 (locked) or 1 (unlocked).

    Methods:
        wait: Wait for the semaphore to become available (value = 1). If the semaphore is not available, this method will block until it is.
        signal: Signal that the semaphore is available (set value to 1).

    Usage:
        semaphore = BinarySemaphore()
        semaphore.wait()  # Wait for the semaphore
        semaphore.signal()  # Signal that the semaphore is available
    """

    def __init__(self):
        self.value = FREE
        self.queue = []

    def wait(self,thread):
        """
        Wait for the semaphore to become available (value = 1).
        If the semaphore is not available, this method will block until it is.
        """
        while self.value == BUSY:
            self.queue.append(thread)  # Add the current thread to the queue
            thread.sleep()  # Put the thread to sleep
        self.value = BUSY

    def signal(self):
        """
        Signal that the semaphore is available (set value to 1).
        """
        if self.queue:
            thread_to_wake = self.queue.pop(0)
            thread_to_wake.wake_up()  # Wake up the waiting thread
        else:
            self.value = FREE


class CountingSemaphore(Semaphore):
    """
    Counting Semaphore

    This class implements a counting semaphore, which allows multiple threads to access a limited pool of resources simultaneously.

    Methods:
        wait: Wait for the semaphore to become available (value > 0). If the semaphore is not available, this method will block until it is.
        signal: Signal that the semaphore is available or release a resource (increment value by 1).

    Usage:
        semaphore = CountingSemaphore(3)  # Initialize with an initial count of 3
        semaphore.wait()  # Wait for the semaphore
        semaphore.signal()  # Signal that the semaphore is available
    """

    def __init__(self, initial_count):
        self.count = initial_count
        self.queue = []

    def wait(self,thread):
        """
        Wait for the semaphore to become available (value > 0).
        If the semaphore is not available, this method will block until it is.
        """
        while self.count == BUSY:
            self.queue.append(thread)  # Add the current thread to the queue
            thread.sleep()  # Put the thread to sleep
        self.count -= 1

    def signal(self):
        """
        Signal that the semaphore is available or release a resource (increment value by 1).
        """
        if self.queue:
            thread_to_wake = self.queue.pop(0)
            thread_to_wake.wake_up()  # Wake up the waiting thread
        else:
            self.count += 1


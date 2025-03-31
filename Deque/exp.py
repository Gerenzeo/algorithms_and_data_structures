from typing import Any
from collections import deque

class Deque:
    """
    A class to represent a deque (double-ended queue).
    Uses the deque from Python's standard library for implementation.
    """

    def __init__(self):
        """
        Initializes an empty deque.
        """
        self.deque = deque()
    
    def append(self, item: Any):
        """
        Adds an element to the end of the deque.

        Arguments:
            item (Any): The element to be added to the end of the deque.
        """
        self.deque.append(item)

    def appendleft(self, item: Any):
        """
        Adds an element to the front of the deque.

        Arguments:
            item (Any): The element to be added to the front of the deque.
        """
        self.deque.appendleft(item)

    def is_empty(self):
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return not self.deque

    def pop(self):
        """
        Removes and returns an element from the end of the deque.

        Exceptions:
            IndexError: Raised if the deque is empty.
        
        Returns:
            Any: The element removed from the end of the deque.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop()

    def popleft(self):
        """
        Removes and returns an element from the front of the deque.

        Exceptions:
            IndexError: Raised if the deque is empty.
        
        Returns:
            Any: The element removed from the front of the deque.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.popleft()
    
    def index(self, item, start=None, end=None):
        """
        Finds the index of the first occurrence of an element in the deque within the specified range.

        Arguments:
            item (Any): The element to search for.
            start (int, optional): The index to start searching from (default is 0).
            end (int, optional): The index to stop searching at (default is the length of the deque).
        
        Exceptions:
            ValueError: Raised if the item is not found within the specified range.

        Returns:
            int: The index of the first occurrence of the item.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        start = start if start is not None else 0
        end = end if end is not None else len(self.deque)

        try:
            return self.deque.index(item, start, end)
        except ValueError:
            raise ValueError(f"Item {item} not found in the deque")
    
    def count(self, item):
        """
        Counts the number of occurrences of an element in the deque.

        Arguments:
            item (Any): The element to count.

        Returns:
            int: The count of occurrences of the item.
        """
        if self.is_empty():
            return 0
        
        count = 0
        for element in self.deque:
            if element == item:
                count += 1
        return count
    
    def size(self):
        """
        Returns the number of elements in the deque.

        Returns:
            int: The size of the deque.
        """
        return len(self.deque)

    def reverse(self):
        """
        Reverses the order of elements in the deque in place.
        """
        self.deque.reverse()
    
    def rotate(self, n):
        """
        Rotates the deque by n steps.

        Arguments:
            n (int): The number of steps to rotate the deque.
        """
        self.deque.rotate(n)

    def clear(self):
        """
        Clears all elements from the deque.
        """
        self.deque.clear()
    
    def __iter__(self):
        """
        Returns an iterator for the deque.

        Returns:
            iterator: An iterator over the deque elements.
        """
        return iter(self.deque)
    
    def __str__(self):
        """
        Returns a string representation of the deque.

        Returns:
            str: A string representation of the deque as a list.
        """
        return f"{list(self.deque)}"
from collections import deque

class Queue:
    """
    A simple implementation of a queue using deque.

    This class represents a FIFO (First In, First Out) queue, 
    supporting standard queue operations such as enqueue, dequeue, 
    and checking if the queue is empty.

    Attributes:
        queue (deque): A deque used to store queue elements.
    """

    def __init__(self):
        """
        Initializes an empty queue using deque.

        Attributes:
            queue (deque): The deque structure used for storing queue elements.
        """
        self.queue = deque()

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Args:
            item (Any): The element to be added to the queue.

        Returns:
            None: This method modifies the queue in place.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the first item from the queue.

        Raises:
            IndexError: If the queue is empty.

        Returns:
            Any: The element that was removed from the queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def is_empty(self):
        """
        Checks whether the queue is empty.

        Returns:
            bool: True if the queue is empty, otherwise False.
        """
        return not self.queue

    def peek(self):
        """
        Returns the first item in the queue without removing it.

        Raises:
            IndexError: If the queue is empty.

        Returns:
            Any: The first element in the queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    def size(self):
        """
        Returns the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.queue)

    def clear(self):
        """
        Removes all elements from the queue.

        Returns:
            None: This method clears the queue in place.
        """
        self.queue.clear()

    def __repr__(self):
        """
        Returns a string representation of the queue.

        This method is used for debugging and represents 
        the queue in a developer-friendly format.

        Returns:
            str: A string that shows the current elements of the queue.
        """
        return f"Queue({list(self.queue)})"

    def __str__(self):
        """
        Returns a user-friendly string representation of the queue.

        This method is used for displaying the queue in a readable format.

        Returns:
            str: A string showing the elements of the queue.
        """
        return f"{list(self.queue)}"

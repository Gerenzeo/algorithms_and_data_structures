class Array:
    """
    A simple dynamic array implementation.

    This class simulates a dynamic array that supports operations
    like appending elements, getting elements by index, and removing elements.
    The array automatically resizes as needed when elements are added.

    Attributes:
        data (list): A list used to store the array elements.
        size (int): The number of elements currently in the array.
    """

    def __init__(self):
        """
        Initializes a new dynamic array.

        This constructor initializes the array with an empty list
        and sets the size to 0.

        Attributes:
            data (list): The list that holds the elements of the array.
            size (int): The number of elements currently in the array.
        """
        self.data = []
        self.size = 0

    def append(self, value):
        """
        Adds an element to the end of the array.

        Args:
            value (Any): The element to be added to the array.

        Returns:
            None: This method does not return any value; it modifies the array in place.
        """
        self.data.append(value)
        self.size += 1
    
    def remove(self, value):
        """
        Remove element by value of the array.

        Args:
            value (Any): The value of the element to remove from the array.
        
        Returns:
            None: This method does not return any value;
        """
        if value in self.data:
            self.data.remove(value)
            self.size -= 1
        else:
            print("Element not found")
    
    def __repr__(self):
        """
        Returns a string representation of the array.

        This method is used to provide a human-readable string
        representation of the array when printed or logged.

        Returns:
            str: A string that shows the current elements of the array.
        """
        return str(self.data)
    
    def __len__(self):
        """
        Returns the number of elements in the array.

        This method allows the use of the 'len()' function on the array object

        Returns:
            int: The number of elements in the array.
        """
        return self.size
    

    def __getitem__(self, index):
        """
        Retrieves an element at the specified index.

        Args:
            index (int): The index of the element to retrieve.

        Raises:
            IndexError: If the index is out of range.

        Returns:
            Any: The element at the specified index.
        """

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index, value):
        """
        Sets the element at the specified index.

        This method allows modifying elements of the array using indexing.

        Args:
            index (int): The index of the element to modify.
            value (Any): The new value of assign to the element.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value

    def __iter__(self):
        """
        Returns an iterator for the array.

        This method allows the array to be used in a for loop or any other
        construct that requires an iterable.

        Returns:
            iterator: An iterator over the array elements.
        """
        return iter(self.data)
    
    def __contains__(self, value):
        """
        Checks if an element is in the array.
        
        This method allows using 'in' operator to check if an element
        exists in the array.

        Args:
            value (Any): The element to check for existense.

        Returns:
            bool: True if element exists in the array. False othewise.
        """
        return value in self.data
    

    def __str__(self):
        """
        Returns a string representation of the array.

        This method is used to provide a readble string representation of the
        array for easy visualization.

        Returns:
            str: A string showing the elements of the array.
        """
        return f"Array({self.data})"
    
    def __eq__(self, other):
        """
        Compares the array with another array for equality.

        This nethod allows using the '==' operator to compare two arrays.

        Args:
            other (Array): Another Array object to compare.

        Returns:
            bool: True if the arrays have the same elements, False otherwise.
        """
        if isinstance(other, Array):
            return self.data == other.data
        return False

    def __add__(self, other):
        """
        Concatenates two arrays.

        This method allows using the '+' operator to combine two arrays into one,
        creating a new array that contains of elemens of both.

        Args:
            other (Array): The array to concatenate with.

        Returns:
            Array: A new array containing elements from both arrays
        """

        if isinstance(other, Array):
            new_array = Array()
            new_array.data = self.data + other.data
            new_array.size = len(new_array.data)
            return new_array
        raise TypeError("Unsuported operand type(s) for +: 'Array' and 'Array'")

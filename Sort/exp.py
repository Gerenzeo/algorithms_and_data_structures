class Sort:
    """
    A simple dynamic sort implementation.

    This class provides implementations for four common sorting algorithms:
        - Bubble Sort
        - Selection Sort
        - Quick Sort
        - Merge Sort 

    Attributes:
        data (list): A list of elements to be sorted.
    """
    
    def __init__(self, data: list):
        """
        Initializes the Sort class with a list of data.

        Args:
            data (list): The list of elements to be sorted.
        """
        self.data = data

    def bubble_sort(self):
        """
        Sorts the list using the Bubble Sort algorithm.

        Returns:
            list: The sorted list.
        """
        if len(self.data) <= 1:
            return self.data
        
        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

    def select_sort(self):
        """
        Sorts the list using the Selection Sort algorithm.

        Returns:
            list: The sorted list.
        """
        if len(self.data) <= 1:
            return self.data
        
        for i in range(len(self.data)):
            min_value, min_index = self.data[i], i
            for j in range(i + 1, len(self.data)):
                if min_value > self.data[j]:
                    min_value, min_index = self.data[j], j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
        return self.data
    
    def quick_sort(self, data: list) -> list:
        """
        Sorts the list using the Quick Sort algorithm (recursive implementation).

        Args:
            data (list): The list of elements to be sorted.

        Returns:
            list: The sorted list.
        """
        if len(data) <= 1:
            return data

        left_data = []  # Elements smaller than pivot
        right_data = []  # Elements greater than pivot
        pivot = data[-1]  # Choosing last element as pivot

        for element in data[:-1]:  # Exclude pivot when iterating
            if element < pivot:
                left_data.append(element)
            else:
                right_data.append(element)

        sorted_left_data = self.quick_sort(left_data)
        sorted_right_data = self.quick_sort(right_data)

        return sorted_left_data + [pivot] * data.count(pivot) + sorted_right_data
    
    def merge_sort(self, data: list) -> list:
        """
        Sorts the list using the Merge Sort algorithm (recursive implementation).

        Args:
            data (list): The list of elements to be sorted.

        Returns:
            list: The sorted list.
        """
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]

        sorted_left_data = self.merge_sort(left_data)
        sorted_right_data = self.merge_sort(right_data)

        def merge(left: list, right: list) -> list:
            """
            Merges two sorted lists into one sorted list.

            Args:
                left (list): The first sorted list.
                right (list): The second sorted list.

            Returns:
                list: A merged sorted list.
            """
            merged = []
            while left and right:
                if left[0] < right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
            merged.extend(left)
            merged.extend(right)
            return merged
    
        return merge(sorted_left_data, sorted_right_data)
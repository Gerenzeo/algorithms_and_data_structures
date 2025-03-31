from collections import deque

class BFS:
    """
    A class implementing Breadth-First Search (BFS) to find a seller in a social network.
    """
    
    def __init__(self, data):
        """
        Initializes the BFS object with the given adjacency list.
        
        Args:
            data (dict): A dictionary representing the graph, where keys are person names 
                         and values are dictionaries containing attributes such as 'is_seller' 
                         and a list of friends.
        """
        self.queue: deque = deque()
        self.data: dict = data

    def person_is_seller(self, name):
        """
        Checks if a person is a seller.
        
        Args:
            name (str): The name of the person to check.
        
        Returns:
            bool: True if the person is a seller, False otherwise.
        """
        return self.data.get(name, {}).get("is_seller", False)

    def search(self, name):
        """
        Performs a BFS to find a seller starting from a given person.
        
        Args:
            name (str): The name of the starting person.
        
        Returns:
            str: A message indicating whether a seller was found or not.
        """
        if name not in self.data:
            return "Person not found in the network."

        self.queue.appendleft(self.data[name])

        while self.queue:
            person: dict = self.queue.popleft()
            is_checked = person.get("is_checked")

            if is_checked:
                continue

            if person["is_seller"]:
                return f"Person {person['name']} is a seller!"
            
            for friend in person['friends']:
                if friend in self.data:
                    self.queue.append(self.data[friend])
            
            person["is_checked"] = True

        return "Seller not found!"


if __name__ == "__main__":
    data = {
        "you": {
            "name": "you",
            "is_seller": False,
            "is_checked": False,
            "friends": ["maria", "alex", "bob"],
        },
        "maria": {
            "name": "maria",
            "is_seller": False,
            "is_checked": False,
            "friends": ["bob", "julia", "jacob", "alex"],
        },
        "alex": {
            "name": "alex",
            "is_seller": False,
            "is_checked": False,
            "friends": [],
        },
        "bob": {
            "name": "bob",
            "is_seller": False,
            "is_checked": False,
            "friends": ["paul", "bob", "anna"],
        },
        "julia": {
            "name": "julia",
            "is_seller": True,
            "is_checked": False,
            "friends": ["jacob"],
        },
        "jacob": {
            "name": "jacob",
            "is_seller": False,
            "is_checked": False,
            "friends": ["anna"],
        },
        "anna": {
            "name": "anna",
            "is_seller": False,
            "is_checked": False,
            "friends": ["you"],
        },
        "paul": {
            "name": "paul",
            "is_seller": True,
            "is_checked": False,
            "friends": [],
        },
    }

    bfs = BFS(data)
    result = bfs.search("you")
    print(result)

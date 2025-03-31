from collections import deque

search_queue = deque()

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



search_queue += graph["you"]

print(search_queue)

def person_is_seller(name):
    return name[-1] == "m"

while search_queue:
    person = search_queue.popleft()

    if person_is_seller(person):
        print(f"Person: {person} is a mango seller!")
        break
    else:
        print(f"Adding friends of {person} to queue! {graph[person]}")
        search_queue += graph[person]

        print("\nQueue:", search_queue)
    

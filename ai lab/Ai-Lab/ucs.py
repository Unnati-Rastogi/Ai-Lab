class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):        
        self.queue.append((priority, item))        
        self.queue.sort(key=lambda x: x[0])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) 
        return None

    def is_empty(self):
        return len(self.queue) == 0


def uniform_cost_search(graph, start, goal):
    """
    Uniform Cost Search (UCS)

    Time Complexity: O(E log V)  (with priority queue)
    Space Complexity: O(V)
    """

    pq = PriorityQueue()
    pq.enqueue((start, [start]), 0) 

    visited = {}

    while not pq.is_empty():
        cost, (node, path) = pq.dequeue()


        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost


        if node == goal:
            return cost, path


        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            pq.enqueue((neighbor, path + [neighbor]), new_cost)

    return float("inf"), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

start = 'A'
goal = 'G'

result = uniform_cost_search(graph, start, goal)

print("Cost and Path:", result)
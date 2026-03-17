from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search(BFS)

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """

    visited = set()
    queue = deque([start])

    visited.add(start)

    print("\nBFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ----------- MAIN PROGRAM -----------

# Input: number of nodes
n = int(input("Enter number of nodes: "))

graph = {}

print("\nEnter adjacency list (space-separated neighbors):")
for i in range(n):
    neighbors = list(map(int, input(f"Neighbors of node {i}: ").split()))
    graph[i] = neighbors

# Input: starting node
start = int(input("\nEnter starting node: "))

# Validation (optional but good for lab)
if start not in graph:
    print("Invalid starting node!")
else:
    bfs(graph, start)
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


n = int(input("Enter number of nodes: "))

graph = {}

print("\nEnter adjacency list (space-separated neighbors):")
for i in range(n):
    neighbors = list(map(int, input(f"Neighbors of node {i}: ").split()))
    graph[i] = neighbors

start = int(input("\nEnter starting node: "))

if start not in graph:
    print("Invalid starting node!")
else:
    visited = set()
    print("\nDFS Traversal:", end=" ")
    dfs(graph, start, visited)
def dls(graph, node, goal, depth, visited):
    """
    Depth-Limited Search (used inside IDFS)
    """
    if depth < 0:
        return False

    print(node, end=" ")
    visited.add(node)

    if node == goal:
        return True

    if depth == 0:
        return False

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False


def idfs(graph, start, goal, max_depth):
    """
    Iterative Deepening DFS

    Time Complexity: O(b^d)
    Space Complexity: O(d)

    b = branching factor
    d = depth of solution
    """
    for depth in range(max_depth + 1):
        print(f"\nDepth Level {depth}: ", end="")
        visited = set()

        if dls(graph, start, goal, depth, visited):
            print("\nGoal node found!")
            return

    print("\nGoal node not found within depth limit.")

n = int(input("Enter number of nodes: "))

graph = {}

print("\nEnter adjacency list (space-separated neighbors):")
for i in range(n):
    neighbors = list(map(int, input(f"Neighbors of node {i}: ").split()))
    graph[i] = neighbors

start = int(input("\nEnter start node: "))
goal = int(input("Enter goal node: "))
max_depth = int(input("Enter maximum depth: "))

idfs(graph, start, goal, max_depth)
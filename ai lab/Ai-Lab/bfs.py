from collections import deque

def bfs(tree, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for child in tree.get(node, []):
            queue.append(child)

    return visited


tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

result = bfs(tree, 1)
print("\nBFS:", *result)
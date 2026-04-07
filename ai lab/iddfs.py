def dls(tree, node, depth, visited):
    visited.append(node)

    if depth == 0:
        return

    for child in tree.get(node, []):
        dls(tree, child, depth - 1, visited)


def iddfs(tree, start, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        dls(tree, start, depth, visited)
        print(f"Depth Limit {depth}: Visited nodes {visited}")


tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

max_depth = int(input("Enter maximum depth for IDDFS: "))

iddfs(tree, 1, max_depth)
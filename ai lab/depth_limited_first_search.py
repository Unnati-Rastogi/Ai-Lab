def dls(tree, node, depth, visited):
    visited.append(node)

    if depth == 0:
        return

    for child in tree.get(node, []):
        dls(tree, child, depth - 1, visited)


tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

limit = int(input("Enter depth limit for DLS: "))

visited_dls = []
dls(tree, 1, limit, visited_dls)

print("\nDLS Visited:", visited_dls)
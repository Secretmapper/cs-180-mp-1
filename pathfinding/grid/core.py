def is_inside(grid, node):
    return node[0] >= 0 and node[0] < grid.shape[1] and node[1] >= 0 and node[1] < grid.shape[0]

def find_neighbors(grid, node):
    neighbors = []

    if is_inside(grid, (node[0] - 1, node[1])):
        neighbors.append((node[0] - 1, node[1]))

    if is_inside(grid, (node[0] + 1, node[1])):
        neighbors.append((node[0] + 1, node[1]))

    if is_inside(grid, (node[0], node[1] - 1)):
        neighbors.append((node[0], node[1] - 1))

    if is_inside(grid, (node[0], node[1] + 1)):
        neighbors.append((node[0], node[1] + 1))

    return neighbors

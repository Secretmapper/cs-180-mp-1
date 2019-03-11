def find_walkable_neighbors(grid, node):
    neighbors = []

    if is_valid_neighbor(grid, (node[0] - 1, node[1])):
        neighbors.append((node[0] - 1, node[1]))

    if is_valid_neighbor(grid, (node[0] + 1, node[1])):
        neighbors.append((node[0] + 1, node[1]))

    if is_valid_neighbor(grid, (node[0], node[1] - 1)):
        neighbors.append((node[0], node[1] - 1))

    if is_valid_neighbor(grid, (node[0], node[1] + 1)):
        neighbors.append((node[0], node[1] + 1))

    return neighbors

def is_valid_neighbor(grid, node):
    return is_inside(grid, node) and is_coord_walkable(grid, node)

def is_inside(grid, node):
    return node[0] >= 0 and node[0] < grid.shape[1] and node[1] >= 0 and node[1] < grid.shape[0]

def is_coord_walkable(grid, node):
    return grid[node[1], node[0]] == 1

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

def backtrack(grid, parents, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parents[path[-1]])
    path.reverse()
    return path

def bfs(grid, start, end, with_expansion=False):
    queue, visited, parents = [start], set(), {}
    if with_expansion:
        expansion = []
    while queue:
        curr = queue.pop(0)
        if curr in visited:
            continue
        visited.add(curr)
        neighbors = find_neighbors(grid, curr)
        if with_expansion:
            expansion.append(curr)
        for neighbor in neighbors:
            if neighbor not in visited:
                parents[neighbor] = curr
             # TODO: extract into helper
            is_walkable = grid[neighbor[1], neighbor[0]] == 0
            if is_walkable:
                continue
            if neighbor == end:
                path = backtrack(grid, parents, start, end)

                if with_expansion: return path, expansion
                else: return path
            else:
                queue.append(neighbor)

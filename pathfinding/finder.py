import heapq
from .grid.core import find_neighbors, is_coord_walkable

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
        if with_expansion:
            expansion.append(curr)
        for neighbor in find_neighbors(grid, curr):
            if neighbor not in visited:
                parents[neighbor] = curr
            if not is_coord_walkable(grid, neighbor):
                continue
            if neighbor == end:
                path = backtrack(grid, parents, start, end)

                if with_expansion: return path, expansion
                else: return path
            else:
                queue.append(neighbor)

def dfs(grid, start, end, with_expansion=False):
   stack, visited = [(start, [start])], []
   while stack:
      curr, path = stack.pop()
      if curr == end:
         if with_expansion: return path, visited
         else: return path
      if curr not in visited:
         visited.append(curr)
      for neighbor in find_neighbors(grid, curr):
         if neighbor not in visited and is_coord_walkable(grid, neighbor):
            stack.append((neighbor, path + [neighbor]))

def manhattan_distance(p0, p1):
    return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])

def exists_in_heap(heap, item):
   return item in (x[1] for x in heap)

def astar(grid, start, end, heuristic=manhattan_distance, with_expansion=False):
   queue, visited, parents = set([start]), set(), {}
   g_cost, f_cost = {}, {}

   g_cost[start] = 0
   f_cost[start] = heuristic(start, end)

   if with_expansion:
      expansion = []
   while queue:
      curr = None
      curr_score = None
      # TODO: Turn this into a priority queue?
      for coord in queue:
         if curr == None or f_cost[coord] < curr_score:
            curr_score = f_cost[coord]
            curr = coord

      if curr == end:
          path = backtrack(grid, parents, start, end)

          if with_expansion: return path, expansion
          else: return path

      queue.remove(curr)

      if curr in visited:
         continue

      visited.add(curr)

      if with_expansion:
         expansion.append(curr)

      for neighbor in find_neighbors(grid, curr):
         if neighbor in visited:
            continue
         if not is_coord_walkable(grid, neighbor):
            continue

         g = g_cost[curr] + manhattan_distance(curr, neighbor)

         if neighbor not in queue:
            queue.add(neighbor)
         elif g >= g_cost[neighbor]:
            continue

         parents[neighbor] = curr
         g_cost[neighbor] = g
         f_cost[neighbor] = g + heuristic(neighbor, end)

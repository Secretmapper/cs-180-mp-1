import ast
import time
from .finder import bfs as o_bfs, dfs as o_dfs, astar as o_astar
from .grid import core

paths = [
   'cases/random.txt',
   'cases/maze-y.txt',
   'cases/boxes-galore.txt',
   'cases/logos-patterns.txt',
   'cases/i-<3-cs-180.txt'
]

def get_case_files():
   cases = []
   for path in paths:
      case = open(path, 'r').read().splitlines()
      cases.append((
         ast.literal_eval(case[0]),
         ast.literal_eval(case[1]),
         ast.literal_eval(case[2])
      ))
   return cases

def cost(p0, p1): return 1
def md(p0, p1):
    return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])

def bfs(maze, start, end):
   start_time = time.time()
   path, expansion_num = o_bfs(maze, core.find_walkable_neighbors, start, end, with_expansion_num=True)
   return (start, end, expansion_num, len(path), time.time() - start_time)

def dfs(maze, start, end):
   start_time = time.time()
   path, expansion_num = o_dfs(maze, core.find_walkable_neighbors, start, end, with_expansion_num=True)
   return (start, end, expansion_num, len(path), time.time() - start_time)

def astar(maze, start, end):
   start_time = time.time()
   path, expansion_num = o_astar(maze, core.find_walkable_neighbors, start, end, cost=cost, heuristic=md, with_expansion_num=True)
   return (start, end, expansion_num, len(path), time.time() - start_time)

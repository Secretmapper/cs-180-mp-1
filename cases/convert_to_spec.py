# quick utility script to convert old v0 txt
# to file input spec format

import ast

paths = [
   'random.txt',
   'maze-y.txt',
   'boxes-galore.txt',
   'logos-patterns.txt',
   'i-<3-cs-180.txt'
]

cases = []
for path in paths:
   case = open(path, 'r').read().splitlines()
   new_case = open(path[:-3] + '_new.txt', 'w+')

   new_case.write(case[0] + '\n')
   new_case.write(case[1] + '\n')

   arr = ast.literal_eval(case[2]g
   for a in arr:
       new_case.write(str(a).strip('[]') + '\n')

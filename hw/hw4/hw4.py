from stack import Stack

# vertexes = 15
# edges = [
#   [1,2],      # 0
#   [3],        # 1
#   [4,5],      # 2
#   [6],        # 3
#   [6],        # 4
#   [7],        # 5
#   [8,9],      # 6
#   [8],        # 7
#   [10],       # 8
#   [10],       # 9
#   [11,12],    # 10
#   [],         # 11
#   [13,14],    # 12
#   [],         # 13
#   []          # 14
# ]

vertexes = 15
edges = [
  [1, 2],
  [2],
  [3, 4, 10],
  [7],
  [5, 8],
  [6, 9],
  [7],
  [12, 13],
  [9],
  [6],
  [11],
  [7],
  [13, 14],
  [],
  [13]
]

v0 = 0
u0 = 14

order = Stack()
discovered = [False] * vertexes
paths = [0] * vertexes

def DFS(v):
  for u in edges[v]:
    if (not discovered[u]):
      discovered[u] = True
      DFS(u)
      order.push(u)

DFS(v0)
order.push(v0)

paths[v0] = 1
while (not order.empty):
  v = order.pop()
  for u in edges[v]:
    paths[u] += paths[v]

[ print(f"{i}: {p}") for i, p in enumerate(paths) ]
print("-" * 20)
print(f"{paths[u0]} paths {v0} --> {u0}")

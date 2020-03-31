from queue import Queue
from stack import Stack
from math import inf, log

vertexes = 8
edges = [
  [1, 3, 4],
  [2, 6],
  [6],
  [4],
  [7, 5],
  [7],
  [7],
  []
]

weights = {
  (0, 1): 0.25,
  (0, 3): 0.65,
  (0, 4): 0.2,
  (1, 2): 0.63,
  (1, 6): 0.3,
  (2, 6): 0.64,
  (3, 4): 0.7,
  (4, 7): 0.1,
  (4, 5): 0.35,
  (5, 7): 0.4,
  (6, 7): 1
}

weights_alt = dict()
for key in weights:
  weights_alt[key] = -log(weights[key])

print(weights_alt)

v0 = 0
u0 = 7

prob = [0] * vertexes
predecessors = [None] * vertexes

prob[v0] = 1

queue = Queue(list(range(vertexes)))
while (not queue.empty):
  v = queue.dequeue()
  print(v)

  for u in edges[v]:
    if (prob[u] < prob[v] * weights[(v, u)]):
      prob[u] = prob[v] * weights[(v, u)]
      predecessors[u] = v
      queue.enqueue(u)

[print(f"{i}: {d}") for i,d in enumerate(prob)]

path = []
while (u0 is not None):
  path.append(u0)
  u0 = predecessors[u0]

print(path[::-1])
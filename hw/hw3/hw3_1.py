from queue import Queue

def detect_cycle(v0, u0, V, E):
  visited = [False] * V
  visited[v0] = True
  predecessors = [None] * V

  queue = Queue()
  queue.enqueue(v0)
  while (not queue.empty):
    v = queue.dequeue()
    for u in E[v]:
      if (v == v0 and u == u0):
        continue
      if (not visited[u]):
        visited[u] = True
        predecessors[u] = v

        if (u == u0):
          res = [u0]
          while (predecessors[res[-1]] is not None):
            res.append(predecessors[res[-1]])
          res.append(u0)
          return res
        
        queue.enqueue(u)


  return None 

V = 8

E = [
  [1, 4],         # 0
  [0, 3],         # 1
  [3, 6],         # 2
  [1, 2, 5],      # 3
  [0, 5, 7],      # 4
  [3, 4, 6, 7],   # 5
  [2, 5],         # 6
  [4, 5]          # 7
]

P = detect_cycle(3, 1, V, E)
print(P)
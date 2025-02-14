#q1 bfs
from collections import deque

def find_shortest_path(matrix):
 # Directions: Up, Down, Left, Right
 directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 # Initialize starting and ending positions
 start = (1, 1)
 end = (4, 4)
 rows = len(matrix)
 cols = len(matrix[0])
 moves = 0
 # Initialize data structures for BFS
 queue = deque([(start, [start])])
 visited = set() # Track visited positions

 while queue:
  (x, y), path = queue.popleft()

  if (x, y) == end:
   return path

  if (x, y) in visited:
   continue
  visited.add((x, y))

  for dist_x, dist_y in directions:
   nx = x + dist_x
   ny = y + dist_y

   if nx >= 0 and nx < rows and ny >= 0 and ny < cols and matrix[nx][ny] == 0:
    queue.append(((nx, ny), path + [(nx, ny)]))
    moves += 1

 print(moves)

 return None

matrix = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0],
]

print(find_shortest_path(matrix))
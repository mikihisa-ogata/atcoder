# over wrapping sheet

import numpy as np

n = int(input())
grid = np.zeros((100, 100))

for i in range(n):
  a, b, c, d = map(int, input().split())
  for j in range(a, b):
    for k in range(c, d):
        grid[j][k] = 1

print(int(sum(sum(grid))))
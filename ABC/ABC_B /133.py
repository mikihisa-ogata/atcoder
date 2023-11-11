# good distance

import math

N, D = map(int, input().split())
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))

print(x)

count = 0
distance = 0
for i in range(N-1):
    for j in range(i+1, N): # 範囲どうなっている？
        for k in range(D):
            distance += abs(x[i][k]-x[j][k]) ** 2
            print(i, j, k)
        distance = math.sqrt(distance)
        if distance.is_integer():
            count += 1
        distance = 0

print(count)
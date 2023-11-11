import numpy as np

H, W = map(int, input().split())

S = []
for i in range(H):
    S.append(input())

x = np.zeros((H, W))

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            for m in range(i-1, i+2):
                for n in range(j-1, j+2):
                    x[m][n] += 1

print(x)

# むずい 一旦後回し
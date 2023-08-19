# coverage

from itertools import product

# 入力
N, M = map(int, input().split())
len = [[] for i in range(M)]
C = [[] for i in range(M)]
for i in range(M):
    len[i] = int(input())
    C[i] = set(map(int, input().split()))

# ビット全探索
bit = []
for A in product(range(2), repeat=N):
    bit.append(list(A))

# 答え
result = 0

check = set(range(1, N + 1))

for i in range(2**N):
    cur = set() #空集合

    for j in range(N):
        if bit[i][j] == 1:
            cur = cur | C[j]
    if check == cur:
        result += 1

print(result)
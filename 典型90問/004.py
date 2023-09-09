# cross sum

# import numpy as np

# H, W = map(int, input().split())
# A = []
# result = []

# for _ in range(H):
#     a = list(map(int, input().split()))
#     A.append(a)

# A = np.array(A)
# B = np.ones((H, W))

# column = np.sum(A, axis=0)
# row = np.sum(A, axis=1)

# for i in range(H):
#     for j in range(W):
#         B[i][j] = row[i] + column[j] - A[i][j]

# for b1 in B:
#     for b2 in b1:
#         print(int(b2), end=' ')
#     print('')

# 入力
h, w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))
ans = [[0] * w for _ in range(h)]
print(ans)

# 縦の列ごとに合計を前計算する
y = [0] * w
for i in range(w):
    cnt = 0
    for j in range(h):
        cnt += a[j][i]
    y[i] = cnt

# 縦の行ごとに合計を前計算する
x = [0] * h
for i in range(h):
    cnt = 0
    for j in range(w):
        cnt += a[i][j]
    x[i] = cnt

for i in range(h):
    for j in range(w):
        ans[i][j] = (x[i] + y[j]) - a[i][j]

for i in range(h):
    print(*ans[i])
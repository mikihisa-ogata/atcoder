# 入力
h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))
ans = [[0] * w for i in range(h)]

y = [0] * w
x = [0] * h

# 列の総和
for i in range(w):
    cnt = 0
    for j in range(h):
        cnt += a[j][i]
    y[i] = cnt

# 行の総和
for i in range(h):
    cnt = 0
    for j in range(w):
        cnt += a[i][j]
    x[i] = cnt

# 答えを格納
for i in range(h):
    for j in range(w):
        ans[i][j] = y[j] + x[i] - a[i][j]

for i in range(h):
    print(*ans[i])

print(a)
print(x)
print(y)
print(ans)

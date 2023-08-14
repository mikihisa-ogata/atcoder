# virus

from collections import deque

n, d = map(int, input().split())
x = []
y = []

for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

# print(x, y)

graph = [[False for _ in range(n)] for _ in range(n)]
print(graph)

# 陽性はTrue
for i in range(n):
    for j in range(n):
        if (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= d ** 2:
            graph[i][j] = True
print(f'graph={graph}')

ans = [False] * n
ans[0] = True
que = deque([0]) # dequeはlistみたいなもの。両端の要素の処理速度が速い。両端でないならリストが良い。
print(f'ans={ans}, que={que}')

while que:
    q = que.popleft() # 0番目の要素をqueから削除してqに入れる
    for i in range(n):
        if graph[q][i] and not ans[i]:
            ans[i] = True
            que.append(i)

for i in range(n):
    print("Yes" if ans[i] else "No")

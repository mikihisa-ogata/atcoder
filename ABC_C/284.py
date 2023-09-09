def dfs(n):
    visited[n] = True
    for val in  G[n]:
        if visited[val]:
            continue
        dfs(val)
 
N, M = map(int,input().split())
G = [[] for _ in range(N+1)]

# グラフ作成
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
 
visited = [False for _ in range(N+1)]
cnt = 0
 
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)
 
print(cnt)

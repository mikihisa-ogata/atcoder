# グラフ

N, M = map(int, input().split())

G = [[] for i in range(N)]
print(G)

for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    print(G)
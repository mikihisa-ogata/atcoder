# peaks

N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    # A -= 1
    # B -= 1
    G[A-1].append(B)
    G[B-1].append(A)

print(G)

ans = 0
for i in range(N):
    height = 0
    for j in G[i]:
        j -= 1
        height = max(height, H[j])
    if H[i] > height:
        ans += 1

print(ans)
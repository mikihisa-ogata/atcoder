# management

N = int(input())
A = list(map(int, input().split()))

G = [0 ]* N

for i in range(N - 1):
    G[A[i] - 1] += 1

for i in range(N):
    print(G[i])
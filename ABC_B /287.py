# postal card

N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(int(input()))

T = []
for i in range(M):
    T.append(int(input()))

result = 0
for i in range(N):
    for j in range(M):
        if S[i] % 1000 == T[j]:
            result += 1
            break

print(result)
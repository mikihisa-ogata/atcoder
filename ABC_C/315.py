# flavors


N = int(input())
F = []
S = []
for i in range(N):
    f, s = map(int, input().split())
    F.append(f)
    S.append(s)

score = []

for i in range(N):
    for j in range(i + 1, N):
          
        if j == i:
            break
        
        if F[i] == F[j]:
            score.append(max(S[i], S[j]) + (min(S[i], S[j]) / 2))
        else:
            score.append(S[i] + S[j])

print(int(max(score)))

# for i in range(N):
#     for j in range(i, N):
#         print(i, j)
#         if j == i:
#             break
        
#         if F[i] == F[j]:
#             score = max(score, max(S[i], S[j]) + min(S[i], S[j]) / 2)
#         else:
#             score = max(score, S[i] + S[j])

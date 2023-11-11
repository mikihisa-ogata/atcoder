# let's get a perfect score

N, M = map(int, input().split())
A = [input() for _ in range(N)]

pair = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(M):
            # print(i, j, k, A[i][k], A[j][k], pair)
            if A[i][k] == "x" and A[j][k] == "x":
                break
            if k == M-1:
                pair += 1

print(pair)

# n, m = map(int, input().split())
# s = [input() for i in range(n)]
# res = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         ok = True
#         for k in range(m):
#             if s[i][k] == 'x' and s[j][k] == 'x':
#                 ok = False
#         if ok:
#             res += 1
# print(res)
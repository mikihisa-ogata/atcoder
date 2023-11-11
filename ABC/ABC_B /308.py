# default price

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

price = 0
for i in range(N):
    for j in range(M):
        if C[i] == D[j]:
            price += P[j+1]
            break
        elif C[i] != D[M-1]:
            price += P[0]
            break
        else:
            pass

print(price)


# n, m = map(int, input().split())
# c = list(input().split())
# d = list(input().split())
# p = list(map(int, input().split()))
# ans = 0
# for v in c:
#     price = p[0]
#     for j in range(m):
#         if v == d[j]:
#             price = p[j + 1]
#             break
#     ans += price
# print(ans)
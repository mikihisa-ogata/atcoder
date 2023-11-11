# ringo's favorite numbers2

# N = int(input())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if (A[i] - A[j]) % 200 == 0:
#             ans += 1

# print(ans)

N = int(input())
A = list(map(int, input().split()))

exist = [0] * 200

ans = 0
for i in range(N):
    j = A[i] % 200
    exist[j] += 1
    if exist[j] >= 2:
        ans += exist[j] - 1
print(ans)
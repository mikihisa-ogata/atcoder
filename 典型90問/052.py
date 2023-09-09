# 052 - Dice Product

n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
ans = 1
for i in range(n):
    s = sum(A[i])
    ans *= s
    ans %= 10 ** 9 + 7
print(ans)
# 069 - Colorful Blocks 2

# n, k = map(int, input().split())

# ans = 0
# mod = 10 ** 9 + 7
# for i in range(n):
#   if i == 0:
#     ans = k
#   elif i == 1:
#     ans *= k - 1
#   else:
#     ans *= k - 2
#   ans %= mod
# print(ans)

n, k = map(int,input().split())
mod = 10 ** 9 + 7
if n == 1:
    print(k)
else:
    ans = k * (k - 1) * pow(k - 2, n - 2, mod)
    print(ans % mod)
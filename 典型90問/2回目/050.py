n, l = map(int, input().split())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n + 1):
  if i == 0:
    dp[i] == 1
  elif i >= 1 and i < l:
    dp[i] = dp[i - 1]
  else:
    dp[i] = dp[i - 1] + dp[i - l]

print(dp[n] % (10 ** 9 + 7))
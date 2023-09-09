N = int(input())
dp = dict()
print(dp)
dp[0] = 0
print(dp)

# 全探索
for x in range(N-1):
    for j, c in enumerate(map(int, input().split())):
        print(j, c)
        y = x + 1 + j
        pre = [*dp.items()]
        for p, cost in pre:
            if p >> x & 1 or p >> y & 1:
                continue
            p |= (1 << x) | (1 << y)
            dp[p] = max(dp.setdefault(p, 0), c + cost)
print(max(dp.values()))

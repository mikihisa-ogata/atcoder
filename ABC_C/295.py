# socks
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

num = defaultdict(int)

for s in A:
    num[s] += 1

ans = 0
for key in num:
    ans += num[key] // 2

print(ans)
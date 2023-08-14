# ABC 137 C green bin

from collections import defaultdict

N = int(input())

# num[s] : 文字列sが何個あるか
num = defaultdict(int)
for _ in range(N):
    s = "".join(sorted(input()))
    num[s] += 1

# 集計 nC2
result = 0
for s in num:
    n = num[s]
    result += n * (n-1) // 2

print(result)
import bisect

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# a.sort()
b.sort()

kumi = n * m
ans = 0

for i in range(n):
  s = p - a[i]
  l = bisect.bisect_left(b, s)
  ans += sum(b[:l]) + a[i] * l
  kumi -= l

ans += kumi * p
print(ans)
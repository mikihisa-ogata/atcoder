# full moon

n, m, p = map(int, input().split())
ans = 0

while True:
  if m <= n:
    ans += 1
    m += p
  else:
    print(ans)
    exit()
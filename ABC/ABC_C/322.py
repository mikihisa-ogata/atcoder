n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
  print(a[cnt] - i - 1)
  if a[cnt] - i == 1:
    cnt += 1
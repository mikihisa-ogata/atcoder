# blue spring

n, d, p = map(int, input().split())
f = list(map(int, input().split()))

ticket_price = round(p / d, 1)
f.sort(reverse=True)
num = 0

for i in range(n):
  if ticket_price < f[i]:
    num += 1
  else:
    break
print(f, num)

num -= num % d
ans = sum(f[num:]) + p * num / d

num2 = num + d
ans2 = sum(f[num2:]) + p * num2 / d

ans = min(ans, ans2)
print(int(ans))
# 084 - There are two types of characters

n = int(input())
s = input()

ans = 0
l = [0]
for i in range(n - 1):
  if s[i] != s [i + 1]:
    l.append(i + 1)

for i in range(1, len(l)):
  ans += (l[i] - l[i - 1]) * (n - l[i])

print(ans)
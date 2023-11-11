a = list((input().split()))
n = int(a[0])
t = a[1]
len_t = len(t)
S = []
for i in range(n):
  S.append(input())

cnt = 1
ans = 0
l = []
for s in S:
  
  flag = False

  # 長さが同じ
  if len(s) == len_t:
    if s == t:
      flag = True
    else:
      for i in range(len_t):
        if s[i] != t[i]:
          if s[:i] + s[i+1:] == t[:i] + t[i+1:]:
            flag = True
            break

  # 長さ1短い
  elif len(s) == len_t - 1:
    for i in range(len_t - 1):
      if s[i] != t[i]:
        if s == t[:i] + t[i+1:]:
          flag = True
      elif s == t[:len_t - 1]:
          flag = True

  # 長さ1長い
  elif len(s) == len_t + 1:
    for i in range(len_t):
      if s[i] != t[i]:
        if s[:i] + s[i+1:] == t:
          flag = True

  if flag == True:
    ans += 1
    l.append(cnt)
  
  cnt += 1

print(ans)
print(*l)
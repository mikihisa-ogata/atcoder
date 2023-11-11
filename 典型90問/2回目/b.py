n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if n == 3:
  if a[1] < x:
    print(-1)
  elif a[1] >= x:
    if a[0] < x:
      print(x)
    elif a[0] >= x:
      print(0)


else:
  score = sum(a[1 : n - 2])
  ans = x - score
  if score + a[-1] < x or x - score > 100:
    print(-1)
  elif score + a[0] >= x:
    print(0)
  else:
    print(x - score)
    
# else:
#   score = sum(a[1 : n - 2])
#   ans = x - score
#   if ans < 0 or ans < a[1]:
#     print(0)
#   elif ans > 100 or ans > a[-1]:
#     print(-1)
#   else:
#     print(ans)
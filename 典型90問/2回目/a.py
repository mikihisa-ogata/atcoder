n = int(input())
x = [int(a) for a in str(n)]

if len(x) == 1:
  print("Yes")
else:
  for i in range(len(x) - 1):
    if x[i] <= x[i + 1]:
      print("No")
      exit()
  print("Yes")
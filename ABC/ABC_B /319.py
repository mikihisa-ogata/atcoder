n = int(input())

li = []

for i in range(1,10):
  if n % i == 0:
    li.append(i)

ans = ""

for i in range(n + 1):
  for j in range(len(li)):
    if i % (n/li[j]) == 0:
      ans += str(li[j])
      break
    elif j == len(li) - 1:
      ans += "-"
      break

print(ans)
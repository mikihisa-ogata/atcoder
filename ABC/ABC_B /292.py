# yellow and red card

N, Q = map(int, input().split())

player = [0] * N
print(player)

for i in range(Q):
  l = list(map(int, input().split()))
  print(l, l[0], l[1])
  if l[0] == 1:
    player[l[1]-1] += 1
  elif l[0] == 2:
    player[l[1]-1] += 2
  elif l[0] == 3:
    print('Yes' if player[l[1]-1] >= 2 else 'No')

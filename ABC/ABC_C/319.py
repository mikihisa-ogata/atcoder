# 入力
C = []
for i in range(3):
  C.extend(list(map(int, input().split())))
  C.sort()

print(C)

bunbo = 362880
bunsi = 0

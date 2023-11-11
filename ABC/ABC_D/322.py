import numpy as np
from itertools import permutations

# 入力
n, k, p = map(int, input().split())
inf = []
for i in range(n):
  a = list(map(int, input().split()))
  inf.append(a)

# 可能かどうかの判定
nums = np.array(inf)
columns_sum = nums.sum(axis=0)
if min(columns_sum[1:]) < p:
  print(-1)
  exit()

# 答え
ans = 10 ** 9

# 順列全探索
for i in permutations(range(n)):
  cost = 0
  score = [p * (-1)] * k

  for j in i:
    # コストの足し算
    cost += inf[j][0]

    # スコアの足し算
    for l in range(k):
      score[l] += inf[j][l + 1]

    # 要素の最小値が0以上だったら
    if min(score) >= 0:
      ans = min(ans, cost)
      break

print(ans)
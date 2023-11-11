from itertools import product

N = 3
for A in product(range(2), repeat=N):
    print(list(A)) # リスト
    print(A) # タプル

# 出力
# [0, 0, 0]
# [0, 0, 1]
# [0, 1, 0]
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 1]
# [1, 1, 0]
# [1, 1, 1]
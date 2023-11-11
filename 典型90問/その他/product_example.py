from itertools import product

n = int(input())
ans = []

for i in product([0, 1], repeat=n):  # 0 -> （ , 1 -> ）
    print(i)

# n=4の時
# (0, 0, 0, 0)
# (0, 0, 0, 1)
# (0, 0, 1, 0)
# (0, 0, 1, 1)
# (0, 1, 0, 0)
# (0, 1, 0, 1)
# (0, 1, 1, 0)
# (0, 1, 1, 1)
# (1, 0, 0, 0)
# (1, 0, 0, 1)
# (1, 0, 1, 0)
# (1, 0, 1, 1)
# (1, 1, 0, 0)
# (1, 1, 0, 1)
# (1, 1, 1, 0)
# (1, 1, 1, 1)

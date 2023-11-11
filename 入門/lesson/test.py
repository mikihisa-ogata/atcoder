from collections import defaultdict

a = ["cat", "cow", "dog", "cow", "lion", "zebra", "cow"]

# 連想配列 num[文字列]=個数
num = defaultdict(int)

for s in a:
    num[s] += 1

for key in num:
    print(key, num[key])

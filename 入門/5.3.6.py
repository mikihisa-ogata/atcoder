# 連想配列

from collections import defaultdict

# 文字列データ
a = ["cat", "cow", "dog", "lion", "zeebra", "cow"]

# 連想配列（num[文字列]=個数）
# int型を指定することで、num[s]のデフォルト値は0になる
num = defaultdict(int)

# 度数分布
for s in a:
    num[s] += 1

# 度数分布の出力
for key in num:
    print(key, num[key])
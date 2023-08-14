# 二つの整数の積の偶奇の判定
a, b = map(int, input().split())
if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')
# 言い換え

N = int(input())
A = list(map(int, input().split()))

#マイナスの個数
num_minus = sum(v < 0 for v in A)

# N個の絶対値の総和、最小値
sum_abs = sum(map(abs, A))
min_abs = min(map(abs, A))

# マイナスの偶奇に応じて出力
print(sum_abs if num_minus % 2 == 0 else sum_abs - min_abs * 2)
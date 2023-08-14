# water station

# N = int(input())

# if N % 5 == 0:
#     print(N)
# else:
#     N += 5 - (N % 5) 
#     print(N)

# 不正解 Nに最も近い5の倍数を出力する問題

N = int(input())
print(round(N / 5) * 5)
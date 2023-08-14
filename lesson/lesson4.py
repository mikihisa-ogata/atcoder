# 1回で出せる飛距離がA以上B以下で、ゴルフの飛距離をK倍にしたい。

K = int(input())
A, B = map(int, input().split())

if A // K == B // K:
    print('NG')
else:
    print('OK')

# 解答例と違ったけどこれが最適解だと個人的に思う

# K = int(input())
# A, B = map(int, input().split())

# exist = False

# for i in range(A, B+1):
#     if i % K == 0:
#         exist = True

# print('OK' if exist else 'NG')
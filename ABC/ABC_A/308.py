# New-Scheme

# S = list(map(int, input().split()))

# if not S[0] >= 100 and S[8] <= 675:
#     print("No")
# else:
#   for i in S:
#     if i % 25 != 0:
#         print("No")

# 解答
import sys
s = list(map(int, input().split()))
for i in range(8):
    if i < 7 and s[i] > s[i + 1]:
        print("No")
        sys.exit() # プログラムを終了させる
    if s[i] < 100 or s[i] > 675 or s[i] % 25 != 0:
        print("No")
        sys.exit()
print("Yes")

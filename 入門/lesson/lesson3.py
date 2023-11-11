H, A = map(int, input().split())
n = 0

while H>0:
    H = H - A
    n += 1

print(n)


# 模範解答　こっちの方が計算回数少なさそう

# H, A = map(int, input().split())
# if H % A == 0:
#     print(H // A)        # H // A は小数点以下切り下げ
# else:
#     print(H // A + 1)
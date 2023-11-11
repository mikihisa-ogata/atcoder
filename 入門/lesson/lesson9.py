# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())
# Y = X

# counter = 0
# for i in range(A+1):
#     X = Y
#     X -= 500 * i
#     for j in range(B+1):
#         X -= 100 * j
#         for k in range(C+1):
#             X -= 50 * k
#             print(X)
#             if X == 0:
#               counter += 1
# print(counter)

# Xの値が変動するから少し難しい

A = int(input())
B = int(input())
C = int(input())
X = int(input())

result = 0



for a in range(0, A + 1):
    for b in range(0, B + 1):
        for c in range(0, C + 1):
            if  500 * a + 100 * b + 50 * c == X:
                result += 1

print(result)
# Xは変動させない。最後の条件判定の時に使うだけ
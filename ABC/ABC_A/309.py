# A-Nine

# A, B = map(int, input().split())

# if abs(A - B) == 1 or abs(A - B) == 3:
#     print("Yes")
# else:
#     print("No")

# nine = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# print(nine)

# a = nine.index(1)
# print(nine.index(1))

# 解答
A, B = map(int, input().split())
ra, ca = (A - 1) // 3, (A - 1) % 3 # 3で割った商と余り
rb, cb = (B - 1) // 3, (B - 1) % 3
print('Yes' if ra == rb and ca + 1 == cb else 'No')

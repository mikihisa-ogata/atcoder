import numpy as np

a = [list(map(int, input().split())) for _ in range(9)]
a = np.array(a)
a2 = np.copy(a)
a3 = np.copy(a)
# print(a)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = np.array(c)

flag = True

for i in range(9):
    b = a[:, i]
    b.sort()
    # print(b)
    if not np.array_equal(b, c):
        flag = False

for i in range(9):
    b = a2[i]
    b.sort()
    # print(b)
    if not np.array_equal(b, c):
        flag = False

for i in range(3):
    for j in range(3):
        # b = np.append(a[j][i : i + 3], a[j + 1][i : i + 3])
        # b = np.append(a[j][i : i + 3], a[j + 2][i : i + 3])
        # print(b)
        b = np.concatenate(
            [
                a3[j * 3][i * 3 : i * 3 + 3],
                a3[j * 3 + 1][i * 3 : i * 3 + 3],
                a3[j * 3 + 2][i * 3 : i * 3 + 3],
            ]
        )
        # print(b)
        b.sort()
        # print(b)
        if not np.array_equal(b, c):
            flag = False


if flag:
    print("Yes")
else:
    print("No")

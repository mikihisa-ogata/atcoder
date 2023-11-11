# 018 - Statue of Chokudai
import numpy as np
pi = np.pi

# 入力
t = int(input())
l, x_1, y_1  = map(int, input().split())
q = int(input())
e = [int(input()) for _ in range(q)]

x_2 = [0 for _ in range(q)]
y_2 = []
z_2 = []
for i in range(q):
    y_2.append(-1 * l / 2 * np.sin(2 * pi * e[i] / t))
    z_2.append(l / 2 - np.cos(2 * pi * e[i] / t))

print(y_2)
print(z_2)

# 位置情報
statue = [x_1, y_1, 0]
loc = [x_2, y_2, z_2]
for i in range(q):
    r = (0 - x_1) ** 2 +(y_2[i] - y_1) ** 2 + (z_2[i] - 0) ** 2
    h = z_2[i]
    print(np.degrees(np.arcsin(h / r)), np.arcsin(h / r))
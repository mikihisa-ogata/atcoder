# 038 - Large LCM

from math import lcm

a, b = map(int, input().split())

c = lcm(a, b)
if c <= 10 ** 18:
    print(c)
else:
    print("Large")

# import math
# a, b = map(int,input().split())

# ans = a * b // math.gcd(a, b)
# if ans > 10 ** 18:
#     print("Large")
# else:
#     print(ans)
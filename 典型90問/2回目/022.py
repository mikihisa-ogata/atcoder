from math import gcd

a, b, c = map(int, input().split())
d = gcd(a, b)
e = gcd(d, c)
print(a // e + b // e + c // e - 3)
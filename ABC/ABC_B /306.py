# base 2

a = list(map(int, input().split()))

value = 0
for i in range(len(a)):
    if a[i]:
        value += 2**i

print(value)
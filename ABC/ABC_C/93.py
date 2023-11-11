# same integers

l = list(map(int, input().split()))

max_l = max(l)

dif = 0
for i in range(3):
    dif += max_l - l[i]

print(dif // 2 if dif % 2 == 0 else (dif + 3) // 2)
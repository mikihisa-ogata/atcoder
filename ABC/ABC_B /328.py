n = int(input())
d = list(map(int, input().split()))

count = 0

for i in range(n):
    digit = (i + 1) % 10
    if 0 <= (i + 1) <= 9 or (i + 1) // 10 == (i + 1) % 10:  # 1 2 3 ... 11 22 ... 99
        if digit <= d[i]:
            count += 1
        if (digit * 10 + digit) <= d[i]:
            count += 1

print(count)

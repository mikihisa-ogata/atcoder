b = int(input())

ans = -1

for i in range(1, b + 1):
    if b == i**i:
        ans = i
        print(ans)
        exit()

    if b < i**i:
        print(ans)
        exit()

# lower

N = int(input())
H = list(map(int, input().split()))

i = 0
ans = 0

while i < N:
    j = i + 1

    while j < N and H[j-1] >= H[j]:
        j += 1

    ans = max(ans, j-i-1)
    i = j

print(ans)
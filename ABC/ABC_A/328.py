n, x = map(int, input().split())
s = list(map(int, input().split()))

score = 0
for i in s:
    if i <= x:
        score += i

print(score)

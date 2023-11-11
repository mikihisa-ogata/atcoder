n, q = map(int, input().split())
s = input()

count = [0] * n

for i in range(1, n):
    count[i] = count[i - 1]
    if s[i] == s[i - 1]:
        count[i] += 1

for i in range(q):
    s, f = map(int, input().split())
    print(count[f - 1] - count[s - 1])

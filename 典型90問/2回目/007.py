import bisect

# n:クラス、a:クラスのレーティング、q:生徒、b:生徒のレーティング
n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = []
for _ in range(q):
    b.append(int(input()))

a.sort()
print(a)
cnt = []
cnt.append(bisect.bisect_left(a, b[0]))
cnt.append(bisect.bisect_left(a, b[1]))
cnt.append(bisect.bisect_left(a, b[2]))
print(cnt)

ans = []
for i in range(q):
    loc = bisect.bisect_left(a, b[i])
    if loc == 0:
        ans.append(a[loc] - b[i])
    elif loc == n:
        ans.append(b[i] - a[loc - 1])
    else:
        ans.append(min(a[loc] - b[i], b[i] - a[loc - 1]))

for i in range(q):
    print(ans[i])

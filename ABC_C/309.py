# rotate

n = int(input())
a = []
for _ in range(n):
    s = input()
    row = [int(x) for x in s]
    a.append(row)

ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            if i == 0 and j < n-1:
                ans[i][j+1] = a[i][j]
            if i < n-1 and j == n-1:
                ans[i+1][j] = a[i][j]
            if i == n-1 and j > 0:
                ans[i][j-1] = a[i][j]
            if i > 0 and j == 0:
                ans[i-1][j] = a[i][j]
        else:
            ans[i][j] = a[i][j]

for row in ans:
    print(''.join(str(x) for x in row))

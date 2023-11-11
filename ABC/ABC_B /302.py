# find snuke

n, m = map(int, input().split())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

s = []
for _ in range(n):
    row = input()
    s.append(row)

for i in range(n):
    for j in range(m):
        for k in range(8):
            word = ""
            for t in range(5):
                x = i + t * dx[k]
                y = j + t * dy[k]
                if x < 0 or x >= n or y < 0 or y >= m:
                    break
                word += s[x][y]
            if word == "snuke":
                for t in range(5):
                    x = i + t * dx[k] + 1
                    y = j + t * dy[k] + 1
                    print(x, y)
                exit(0)

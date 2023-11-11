# snuke the cookie picker
import pprint

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

row = []
for i in range(H):
    row.append(S[i].count('#'))

column = []
for j in range(W):
    counter = 0
    for i in range(H):
        if S[i][j] == "#":
            counter += 1
    column.append(counter)

pprint.pprint(S, width=20)
print(row, column)
print(min(row[i] for i in range(H) if row[i] >= 1), min(i for i in column if column[i] >= 1))


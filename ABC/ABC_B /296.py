# chessboard
s = []
for _ in range(8):
    s.append(input())

print(s)
print(s[0], s[0][0])

h, w = 0, 0

for i in range(8):
    for j in range(8):
        if s[i][j] == '*':
            h = abs(8-i)
            w = j

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(abc[w], h, sep='')
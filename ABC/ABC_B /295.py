R, C = map(int, input().split())
B = []
for i in range(R):
    # B.append(list(input().split()))
    # B.append(list(map(str, input().split())))
    B.append(list(input()))

print(R, C, B)

for i in range(R):
    for j in range(C):
        if B[i][j].isdigit():
            print(i, j)
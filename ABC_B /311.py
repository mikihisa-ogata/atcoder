N, D = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

result = [0]
k = 0
for i in range(D):
    for j in range(N):
        flag = True
        if S[j][i] == "x":
            flag = False
            k = 0
            break
    if flag == True:
        k += 1
        result.append(k)

print(max(result))
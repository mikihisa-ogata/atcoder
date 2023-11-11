# tournament result

N = int(input())

A = []
for _ in range(N):
    A.append(input())

answer = "correct"
for i in range(N):
    for j in range(i,N):
        if i == j:
            if A[i][j] == '-':
                continue
            else:
                answer ="incorrect"
                print(answer)
                exit()
        elif i != j:
            if A[i][j] == "W" and A[j][i] =="L":
                continue
            elif A[i][j] == "L" and A[j][i] =="W":
                continue
            elif A[i][j] == "D" and A[j][i] =="D":
                continue
            else:
                answer="incorrect"
                print(answer)
                exit()

print(answer)
          
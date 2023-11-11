# 048 - I will not drop out

n, k = map(int, input().split())
A , B = [], []
C = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    A.append(C[i][1])
    A.append(C[i][0] - C[i][1])

A = sorted(A, reverse=True)
print(sum(A[0:k]))
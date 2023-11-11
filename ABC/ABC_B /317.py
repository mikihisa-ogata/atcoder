# MissingNo

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

for i in range(N):
    if A[i] + 1 != A[i + 1]:
        print(A[i] + 1)
        exit()
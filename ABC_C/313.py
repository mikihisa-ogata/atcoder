# approximate equalization2

N = int(input())
A = list(map(int, input().split()))

ave = sum(A) // len(A)

dif1 = 0
dif2 = 0
for i in range(N):
    if A[i] <= ave:
        dif1 += (ave - A[i])
    elif A[i] > ave + 1:
        dif2 += (A[i] - (ave +1))

print(max(dif1, dif2))
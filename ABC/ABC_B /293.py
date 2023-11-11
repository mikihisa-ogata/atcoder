# call the id number

N = int(input())
O = [num for num in range(1, N+1)]
A = list(map(int, input().split()))

for i in range(N):
    if i+1 in O and A[i] in O:
        O.remove(A[i])
        print(O, A[i])

print(len(O))
for item in O:
    print(item, end=' ')
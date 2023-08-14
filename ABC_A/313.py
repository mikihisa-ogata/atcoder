# to be saikyo

N = int(input())
P = list(map(int, input().split()))

value = 0
for i in range(1,N):
    value = max(value, P[i])

if P[0] > value :
    print(0)
elif P[0] == value:
    print(1)
else:
    print(value - P[0] + 1)
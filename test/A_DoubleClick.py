N, D = map(int, input().split())
T = list(map(int, input().split()))

if all(T[i+1] - T[i] > D for i in range(len(T)-1)):
    print(-1)

for i in range(len(T)-1):
    if T[i+1] - T[i] <= D:
        time = T[i+1]
        print(time)
        break
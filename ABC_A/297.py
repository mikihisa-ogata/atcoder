# double click

N, D = map(int, input().split())
T = list(map(int, input().split()))

time = -1

for i in range(N-1):
    if T[i+1] - T[i] <= D:
        time = T[i+1]
        break
    else:
        pass
    
print(time)
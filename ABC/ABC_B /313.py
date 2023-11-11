# who is saikyo?

N, M = map(int, input().split())
list = list(range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    if b in list:
        list.remove(b)

if len(list) == 1:
    print(list[0])
else:
    print(-1)
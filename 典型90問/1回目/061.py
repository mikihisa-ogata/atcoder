# 061 - Deck（★2)

from collections import deque

Q = int(input())
list = []
deq = deque(list)

for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        deq.appendleft(x)
    elif t == 2:
        deq.append(x)
    elif t == 3:
        print(deq[x - 1])
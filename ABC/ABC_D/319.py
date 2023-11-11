N, M = map(int, input().split())
L = [int(x) for x in input().split()]


def f(w):
    line = 0
    rem = 0
    for i in range(N):
        if L[i] + 1 <= rem:
            rem -= L[i] + 1
        else:
            line += 1
            rem = w - L[i]
            if rem < 0:
                return False
    return line <= M


wa = 0
ac = 1e15

while abs(ac - wa) > 1:
    wj = (ac + wa) // 2
    if f(wj):
        ac = wj
    else:
        wa = wj
print(int(ac))

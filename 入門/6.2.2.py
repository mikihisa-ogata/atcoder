# 再帰関数

def rec(N):
    if N == 0:
        return 0
    
    return N + rec(N-1)

print(rec(100))
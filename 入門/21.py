# christmas

def rec(N, X, L, S):
    if N == 0:
        return 1
    
    if X == 1:
        return 0
    elif X <= L[N - 1] + 1:
        return rec(N - 1, X - 1, L, S)
    elif X == L[N - 1] + 2:
        return S[N -1] + 1
    else:
        return S[N - 1] * 2 + 1
    
# 入力
N, X = map(int, input().split())

# バーガーの長さとパティ数S
L = [1] * (N + 1)
S = [1] * (N + 1)
for n in range(1, N + 1):
    L[n] = L[n - 1] * 2 + 3
    S[n] = S[n - 1] * 2 + 1

# 再帰的に求める
print(rec(N, X, L, S))

# N, X = map(int, input().split())

# burger = "P"

# for i in range(N):
#     burger = "B" + burger + "P" + burger + "B"

# print(burger[0:X].count("P"))
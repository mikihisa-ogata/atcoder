# many requirements

# 入力
N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for q in range(Q):
    a[q], b[q], c[q], d[q] = map(int, input().split())
    a[q] -= 1
    b[q] -= 1

# 数列Aのスコアを計算
def calc_score(A):
               score = 0
               for ai, bi, ci, di in zip(a, b, c, d):
                       if A[bi] - A[ai] == ci:
                               score += di
               return score

# 数列Aを全列挙してスコアの最大値を求める再帰関数
def rec(A):
        if len(A) == N:
                return calc_score(A)
        
        result = 0

        prev_last = A[-1] if A else 1

        for add in range(prev_last, M + 1):
                A.appnd(add)
                result = max(result, rec(A))
                A.pop()
                
        return result

A = []
print(rec(A))
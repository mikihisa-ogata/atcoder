# 累積和
N = int(input())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

print(S)
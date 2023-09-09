# 014 - We Used to Sing a Song Together

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

result = 0
for i in range(N):
    result += abs(A[i] - B[i])

print(result)
# filter

# N = int(input())
# A = list(map(int, input().split()))

# for i in range(N): # for a in A:で回すとより簡単
#     if A[i] % 2 == 0:
#         print(A[i], end=" ")

N = int(input())
A = list(map(int, input().split()))

for a in A:
    # 2 で割ったあまりが 0 なら偶数
    if a % 2 == 0:
        print(a)

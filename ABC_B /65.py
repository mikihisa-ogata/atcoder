# # trained

# N = int(input())
# A = []
# for i in range(N):
#     A.append(int(input()))

# i = 0
# cnt = 0
# flag = []

# for j in range(N):
#     if i == 1:
#         print(cnt)
#         exit()
#     elif i in flag:
#         print(-1)
#         exit()
#     flag.append(i)
#     i = A[i] - 1
#     cnt += 1

import sys

n=int(input())
a=[int(input()) for _ in range(n)]

b=1
for i in range(n):
  b=a[b-1]

  if b==2:
    print(i+1)
    sys.exit()

  if i==n-1:
    print(-1)

# same map in the rpg world

# def rotate(array):
#     return array[1:] + array[:1]

from collections import deque

H, W = map(int, input().split())

A = []
for _ in range(H):
    A.append(list(input().split()))

print(A)

B = []
for _ in range(H):
    B.append(list(input().split()))

print(B)

flag = 'No'
for i in range(H):
    rotate(A)
    for j in range(W):
        rotate(A[0])
        print(A)
        if A == B:
            flag =='True'
            print(flag)
            exit()
            
print(flag)
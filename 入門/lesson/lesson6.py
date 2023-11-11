# N = int(input())
# A = list(map(int, input().split()))

# count = 0
# output = 0

# for i in A:
#     if i % 2 == 0:
#         count += 1
# if count == N:
#     output += 1

# どのようにしてループを回せば良いかわからなかった。
# Aの要素をそれぞれ2で割って格納する方法がわかわなかった
    
# 解答例
N = int(input())
A = list(map(int, input().split()))

counter = 0

while True:
    can_do = True
    for i in range(N):
        if A[i] % 2 == 1:
            can_do = False
    
    if not can_do:
        break

    for i in range(N):
        A[i] //= 2

    counter += 1

print(counter)


# N = int(input())
# A = list(map(int, input().split()))

# counter = 0

# while all(a % 2 == 0 for a in A):
    
#     A = [a // 2 for a in A] #これ a//2 ちゃんと順番に格納される？

#     counter += 1

# print(counter)
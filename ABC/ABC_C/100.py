# *3 or /2

# 素因数2の個数を調べる
def num_of_2(num, A):
    i = 0
    while True:
        if num % 2 != 0:
            A.append(i)
            break
        else:
            num = num / 2
            i += 1

N = int(input())
A = list(map(int, input().split()))

num_2 = []
for i in range(N):
    num_of_2(A[i], num_2)

print(sum(num_2))
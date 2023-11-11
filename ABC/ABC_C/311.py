N = int(input())
A = list(map(int, input().split()))

A.insert(0, 0)
print(A)
num = 1
l = []
while True:
    print(f"num={num}, A[num]={A[num]}, l={l}")
    l.append(A[num])
    num = A[num]
    if A[num] in l:
        l = l[l.index(A[num]):]
        print(len(l))
        for i in range(len(l)):
            print(l[i], end=" ")
        exit()
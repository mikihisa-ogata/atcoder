# longest uncommon prefix

N = int(input())
S = input()

for i in range(N-1):
    l = 0
    for k in range(N-i-1):
        # print(k, k+i+1, S[k], S[k+i+1])
        if S[k] == S[k+i+1]:
            break
        l += 1
    print(l)
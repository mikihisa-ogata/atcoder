# inverse prefix sum

N = int(input())
S = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        print(S[i])
    else:
        print(S[i]-S[i-1])
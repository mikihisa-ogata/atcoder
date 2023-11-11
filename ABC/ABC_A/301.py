# overall winner

N = int(input())
S = input()

takahashi = 0
aoki = 0

for i in range(N):
    if S[i] == "T":
        takahashi += 1
    else:
        aoki += 1

if takahashi > aoki:
    print("T")
elif aoki > takahashi:
    print("A")
elif S[N-1] =="T":
    print("A")
else:
    print("T")
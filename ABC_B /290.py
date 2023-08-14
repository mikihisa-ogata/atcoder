# qual B

N, K = map(int, input().split())
S = input()
T = ""
counter = 0

for i in range(len(S)):
    if S[i] == "o":
        T += "o"
        counter += 1
    else:
        T += "x"
    if counter >= K:
        for i in range(i, len(S)-1):
            T += "x"
        print(T)
        exit()

N = int(input())
S = input()
l = ["A", "B", "C"]
for i in range(len(S)):
    if S[i] in l:
        l.remove(S[i])
    if len(l) == 0:
        print(i+1)
        exit()
# job interview

N = int(input())
S = input()

safe, out = 0, 0

for i in range(N):
    if S[i] == "o":
        safe += 1
    elif S[i] == "x":
        out += 1

if safe >= 1 and out == 0:
    print("Yes")
else:
    print("No")
# probably english

N = int(input())
W = input().split()

answer = "No"
for i in range(N):
    print(W[i], answer)
    if (W[i] == "and") or (W[i] == "not") or (W[i] == "that") or (W[i] == "the") or (W[i] == "you"):
        answer = "Yes"

print(answer)
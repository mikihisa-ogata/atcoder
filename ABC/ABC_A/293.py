# swap odd and even

S = input()

n = len(S) // 2
s = ""
for i in range(n):
    s += S[2*i + 1]
    s += S[2*i]

print(s)
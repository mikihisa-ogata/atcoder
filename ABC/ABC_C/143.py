# slimes

N = int(input())
S = input()

i = 0
ans = 0
while i < N:
    j = i

    while j < N and S[i] == S[j]:
        j += 1

    ans += 1
    i = j

print(ans)
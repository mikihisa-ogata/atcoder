# alternately

N = int(input())
S = input()

output = "Yes"
for i in range(N-1):
        if S[i+1] == S[i]:
              output = "No"
              break

print(output)
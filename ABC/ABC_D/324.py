import itertools
import math

n = int(input())
S = (input())
s = []
for i in range(n):
  s_1 = int(S[i])
  s.append(s_1)

ans = set()
combi = []
combi += list(itertools.permutations(s))
# -> [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
# for i in range(1,n):
#   combi += list(itertools.combinations(s, i))

for com in combi:
  calc = 0
  for i in range(len(com)):
    calc += (10**i) * com[i]
  if calc == int(math.sqrt(calc)) * int(math.sqrt(calc)) and calc != 0:
    ans.add(calc)
    print(calc)

print(ans)
print(len(ans))
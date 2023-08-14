# qualification contest

N, K = map(int, input().split())
s = []
for i in range(N):
    s.append(input())

s = s[0:K]
s.sort()
for item in s:
    print(item)
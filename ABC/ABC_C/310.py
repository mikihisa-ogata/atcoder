# # reversible

# N = int(input())
# S = [input() for i in range(N)]
# s = []
# for i in range(N):
#     s.append(S[i][::-1])

# l = list(range(N))

# for i in l:
#     for j in range(i+1, N):
#         if S[i] == S[j] or S[i] ==s[j]:
#             l.remove(j)

# print(len(l))

N = int(input())
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))
print(len(t))
# gacha

# from collections import defaultdict

# num = defaultdict(int)

# N = int(input())
# S = [input() for _ in range(N)]
# print(N, S)

# sum = 0
# for _ in range(N):
#     num[S] += 1


N = int(input())
s = set(input() for _ in range(N))
print(len(s))
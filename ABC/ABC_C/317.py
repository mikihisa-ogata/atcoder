# remember the day 動的計画法

result = -1

def rec(i, total, result):
    for j in G[i]:
        if not j[0] in visited2:
            visited2.append(j[0])
            total += j[1]
            rec(j[0], total, result)
        else:
            print(visited2, total)
            visited2 = visited
            result = max(result, total)

#入力
N, M = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])

for i in range(N):
   # データの型
   visited = []
   visited2 = []
   total = 0
   visited.append(i + 1)
   visited2.append(i + 1)
   rec(i + 1, total, result)

print(G)
# print(result)


# for j in G[1]:
#     print(j[0])
#     print(j[1])
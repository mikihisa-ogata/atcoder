# double dots

# # 入力
# N, M = map(int, input().split())
# G = [[] for i in range(N + 1)]
# for i in range(M):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)

# print(G)

# # dist 経路長
# dist = [-1] * (N + 1)
# dist[0] = []
# dist[1] = 0
# print(dist)

# cur = 1
# for i in dist[cur]:
#     dist[i] = dist[cur] + 1

# print(dist)

from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]  # 隣接リストを表現するリスト
ans = [0] * N               # 各ノードの親ノードを記録するリスト
vis = [False] * N           # ノードの訪問状態を記録するリスト

def _main():
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        E[a].append(b)  # グラフの辺を登録（無向グラフなので両方の方向に登録）
        E[b].append(a)

    que = deque()
    que.append(0)     # 初期ノード（例では0番目のノード）をキューに追加
    vis[0] = True     # 初期ノードを訪問済みとしてマーク

    while que:
        cu = que.popleft()  # キューからノードを取得
        for to in E[cu]:    # 隣接する各ノードに対して
            if not vis[to]:  # 未訪問の場合
                ans[to] = cu  # 親ノードを記録
                vis[to] = True  # ノードを訪問済みとしてマーク
                que.append(to)  # キューに追加して探索を続ける

    print("Yes")
    for i in range(1, N):
        print(ans[i] + 1)  # 各ノードの親ノードを表示（インデックスを+1して表示）

_main()

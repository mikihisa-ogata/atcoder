# 頂点数、辺数、クエリ数
N, M, Q = map(int, input().split())

# 頂点数Nのグラフの型を作る
G = [[] for i in range(N)]

# 辺の入力
for i in range(M):
    u, v = map(int, input().split())
    # listのインデックスに合わせるため1引く
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

# 色の入力
col = list(map(int, input().split()))

# クエリの処理
for i in range(Q):
    
    # * : Extended Iterable Unpacking 数字があったら拾うイメージ
    t, x, *y = map(int, input().split())

    # 頂点の場所を調節して、色の出力
    x -= 1
    print(col[x])

    #タイプ1の処理
    if t == 1:
        for v in G[x]:
            col[v] = col[x]
    # タイプ2の処理
    else:
        col[x] = y[0]
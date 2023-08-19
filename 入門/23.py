# grid repainting

from queue import Queue

# 上下左右の移動
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

# 入力
H, W = map(int, input().split())
S = [input() for i in range(H)]

que = Queue()
dist = [[-1] * W for i in range(H)]

# 幅優先探索の初期条件
que.put((0, 0))
dist[0][0] = 0

# 幅優先探索
while not que.empty():
    x, y = que.get()

    for dx, dy in zip(DX, DY): # zip(DX, DY) = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x2, y2 = x + dx, y + dy

        # 例外はcontinueで次のループにスキップ
        # はみ出し
        if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W:
            continue
        
        # 黒マスには進めない
        if S[x2][y2] == "#":
            continue
        
        # (x2, y2)がすでに探索済みの場合
        if dist[x2][y2] != -1:
            continue
        
        # (x2, y2)をキューにpushして,distを更新
        que.put((x2, y2))
        dist[x2][y2] = dist[x][y] + 1

# 白マスの数
white = sum(line.count('.') for line in S)

# 答えの出力
if dist[H - 1][W - 1] != -1:
    print(white - dist[H - 1][W - 1] - 1)
    print(dist)
else:
    print(-1)
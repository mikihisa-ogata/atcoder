from queue import Queue

def bfs(start_x, start_y, goal_x, goal_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = Queue()
    q.put((start_x, start_y, 0))  # キューに始点を追加

    visited = set()  # 訪れた位置を記録するセット
    visited.add((start_x, start_y))

    while not q.empty():
        x, y, steps = q.get()  # キューから位置とステップ数を取得
        
        # ゴールに到達した場合
        if x == goal_x and y == goal_y:
            return steps
        
        # 新しい位置への移動
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                q.put((new_x, new_y, steps + 1))
                visited.add((new_x, new_y))
                print(f'que={q}')
                print(f'visited={visited}')
    
    return -1  # ゴールにたどり着けない場合

# 入力
rows, cols = map(int, input().split())
maze = [list(input()) for _ in range(rows)]

# スタートとゴールの座標を探す
for x in range(rows):
    for y in range(cols):
        if maze[x][y] == 'S':
            start_x, start_y = x, y
        elif maze[x][y] == 'G':
            goal_x, goal_y = x, y

# BFSを実行して最短経路を求める
result = bfs(start_x, start_y, goal_x, goal_y)
print(result)

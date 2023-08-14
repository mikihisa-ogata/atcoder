# traveling

def solve():
    # プラン数
    N = int(input())

    # 前回の時刻と座標
    pt, px, py = 0, 0, 0

    # N ステップの移動
    for i in range(N):
        t, x, y = map(int, input().split())
        T, X, Y = t - pt, abs(x - px), abs(y - py)
        if T < X + Y:
            return False
        if T % 2 != (X + Y) % 2:
            return False
        
        # 座標の更新
        pt, px, py = t, x, Y
    
    # 最後まで到達
    return True

print("Yes" if solve() else "No")
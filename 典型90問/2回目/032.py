# import sys
# input = sys.stdin.readline # 入力の形式が少し変わるだけ

from itertools import permutations

# 入力
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
x = [list(map(int,input().split())) for _ in range(m)]

# 仲がいいか悪いかの判別
grid = [[True] * n for _ in range(n)]
# 仲の悪い組だけFalseにする
for i in range(m):
    grid[x[i][0] - 1][x[i][1] - 1] = False
    grid[x[i][1] - 1][x[i][0] - 1] = False
print(grid)

ans = 10 ** 18

# 順列全探索
for i in permutations(range(n)): # n=3 => i = (0,1,2), (0,2,1),...
    Bool = True # flag
    for j in range(n - 1):
        if not grid[i[j]][i[j + 1]]:
            Bool = False
            break # 現在の内側のループの次のステップに入る

    cnt = 0 # リレーが可能な時の合計時間
    if Bool:
        for j in range(n):
            cnt += a[i[j]][j]
        ans = min(ans, cnt)

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
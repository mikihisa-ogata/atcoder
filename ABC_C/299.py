# dango

N = int(input())
S = input()

ans = 0

# 文字列の探索を順番と逆順の2回
for i in range(2):
    # 極大な右ダンゴ文字列のレベルを列挙する
    level = 0
    for i in range(N):
        if S[i] == '-':
            # '-' に対応する極大な右ダンゴ列のレベルは、直前までの 'o' の個数
            ans = max(ans, level)
            level = 0 # lebelの初期化
        else:
            level += 1

    # 文字列を反転
    S = S[::-1]

if ans:
    print(ans)
else:
    print("-1")

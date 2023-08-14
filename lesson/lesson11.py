# N, Y = map(int, input().split())

# for a in range(0, N+1):
#     for b in range(0, N - a + 1):
#         for c in range(0, N - (a + b) + 1):
#             if 1000 * a + 5000 * b + 10000 * c == Y:
#                 print(c, b, a)
                
# aの数が適切に出力されない
# 一つの組み合わせを見つけたら、プログラムを終了させたい
# 組み合わせが見つからなかった時の-1の出力ができない

N, Y = map(int, input().split())

ares, bres, cres = -1, -1, -1

for a in range(N + 1):
    for b in range(N + 1):
        c = N - a - b
        
        if c < 0 or c > N:
            continue
        
        if 10000 * a + 5000 * b + 1000 * c == Y:
            ares, bres, cres = a, b, c

print(ares, bres, cres)

# どうしてa,b,cの組み合わせが複数出てこないのか？一つの組み合わせを見つけて終了するのか？
# 上の疑問理解した。
# 理由はたくさんの組み合わせを探索して入るのだけど、新しい組み合わせを見つけては逐次更新しており、全てのfor文が終了したところでprint関数を1度だけ実行しているから。
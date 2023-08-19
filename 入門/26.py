# summer vacation

from heapq import heappush, heappop

# 入力
N, M = map(int, input().split())

# AtoB[v] : A[i] = v となるiに対するB[i]の集合
AtoB = [[] for i in range(M + 1)]

for i in range(N):
    
    # 仕事の入力
    A, B = map(int, input().split())

    # M日を超えるのは無意味
    if A > M:
        continue
    
    # データ登録
    AtoB[A].append(B)

# 報酬の最大値
result = 0

# ヒープ（優先度付きキュー）
que = []

# M - 1 日目から 0 日目に遡る
for Bs in AtoB:
    
    # ヒープに遡った分の仕事を追加する
    for B in Bs:
        
        # ヒープは小さい順なので符号を反転して追加する
        heappush(que, -B)

    print(que)

    # ヒープが空でなければ報酬最大の仕事を答えに足す
    if que:
        result -= heappop(que)

print(result)
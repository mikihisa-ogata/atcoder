# 再帰関数
# 初期値
N = 2
def rec(A):
    # 終了条件
    if len(A) == N:
        print(A)
        return
    
    for v in range(2):
        A.append(v)
        rec(A)
        A.pop() # Aを元に戻す

rec([])
# 区間分割・連長圧縮
S = input()
N = len(S)

i = 0
while i < N:
    
    j = i

    # j番目とi番目の文字が等しければ1足す、違えば差分を出力する
    while j < N and S[j] == S[i]:
        j += 1

    print(S[i], j - i)

    # iをjに更新
    i = j
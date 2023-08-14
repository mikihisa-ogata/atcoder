# ascii art

H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(map(int, input().split())))

print(S)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(H):
    for j in range(W):
        if S[i][j] == 0:
            S[i][j] = '.'
            print('.', end="")
        else:
            S[i][j] = alpha[S[i][j]-1]
            print(f"{S[i][j]}", end="")
    print('')

# 解説

# import string
# convert = '.' + string.ascii_uppercase
# H, W = map(int, input().split())
# for i in range(H):
#   print(''.join(convert[int(a)] for a in input().split()))
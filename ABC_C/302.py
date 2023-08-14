# 

import itertools



for T in itertools.permutations(S):
    ok = True
    for i in range(N - 1):
        if T[i] と T[i+1] が一文字違いでない:
            ok = False
    if ok:
        print("Yes")
        exit()
print("No")
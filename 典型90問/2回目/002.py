from itertools import product

n = int(input())

# nが奇数だったら終了
if n % 2 != 0:
    exit()

ans = []
for bits in product([1, -1], repeat=n):
    # 0と1の個数が等しい時
    if sum(bits) == 0:
        count = 0
        flag = True
        for i in range(n):
            count += bits[i]
            if count < 0:
                flag = False

        if flag:
            ans.append(bits)

print(ans)
for item in ans:
    cur = ""
    for i in item:
        if i == -1:
            cur += ")"
        else:
            cur += "("
    print(cur)

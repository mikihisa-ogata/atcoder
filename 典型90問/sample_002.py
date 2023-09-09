from itertools import product
n = int(input())
ans = []

for i in product([0, 1], repeat = n): # 0 -> （ , 1 -> ）
    if i.count(1) == n // 2:
        zero_count = 0
        Bool = True
        word = ""
        for j in i:
            if j == 0:
                zero_count += 1
            elif j == 1:
                if zero_count >= 1:
                    zero_count -= 1
                else:
                    Bool = False
            word += str(j)

        if Bool:
            x = word.replace("0", "(")
            y = x.replace("1", ")")
            ans.append(y)

ans.sort()
print(*ans ,sep = "\n")
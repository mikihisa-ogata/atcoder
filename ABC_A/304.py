# first player

# N = int(input())

# S = []
# A = []

# for i in range(N):
#     S.append(input())
#     A.append(int(input()))

# print(S, A)

# 解答 chatgpt

n = int(input())
s = []
a = []

for _ in range(n): # 特に意味がなければforloopは_で回す
    name, value = input().split() #それぞれにinputした後にint()すれば良い
    s.append(name)
    a.append(int(value))

# とりあえずmにa[0]を入れて、それより小さいのがあれば随時更新する mはタプル
m = (a[0], 0) 
# この時点で m = (31, 0)

for i in range(1, n):
    m = min(m, (a[i], i)) 
    # タプルの大小はどうやって比べるの？ 
    # 多分要素の中で最も大きい数が入っているタプルを上書き

p = m[1]

# p番目からスタート
for i in range(n):
    print(s[(p+i)%n])

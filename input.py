# inputの仕方

# 1 2 3 --> ['1', '2', '3'] listの要素のtypeはstr
a = input().split(" ")
print(a, type(a), type(a[0]))


#list型で受け取るとき
# 入力 Alice Bob Charlie
s = input().split()
print(s) # ['Alice', 'Bob', 'Charlie']
print(s[0]) # Alice
print(s[0][0]) # A

#文字列として受け取るとき 
# 入力 Alice Bob Charlie
A, B, C = input().split()
print(A)     # Alice
print(A,B,C) # Alice Bob Charlie


# 入力 1 3
A, B = map(int, input().split())
print(A) #1
print(A,B) # 1 3


#list型で取得
# 入力 1 3 4 5 6
l = list(map(int, input().split()))
print(l) # [1, 3, 4, 5, 6]


# 入力
# 5
# 1 2
# 3 4
# 5 6
# 7 8
# 9 10
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
print(l) # [[1, 2], [3, 4], [5, 6]]


# 入力例
# 5
# 1 a
# 3 b
# 5 c
# 7 d
# 9 e
N = int(input())
list = []
for i in range(N):
    a,b=input().split()
    list.append([int(a), b])
#出力
print(list) # [[1, 'a'], [3, 'b'], [5, 'c'], [7, 'd'], [9, 'e']]
print(type(list[0][0])) # <class'int'>
print(type(list[0][1])) # <class'str'>


# 入力
# 2
# 3 1 2
# 6 1 1
#先に入力変数分の長さを持つlistを作っておく。※N = 5の場合,t = [0,0,0,0,0]
N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    #上から順番に代入していく
    t[i], x[i], y[i] = map(int, input().split())

#出力
print(t) # [3, 6]

# treasure chest

N = int(input())
S = input()

l = []
for i in range(N):
    if S[i] == "|":
        l.append(i)

output = "out"
for i in range(l[0], l[1]+1):
    if S[i] == "*":
        output = "in"
        break
    
print(output)

# 解答

# N = int(input())
# S = input()
# v_first = S.index('|')
# s = S.index('*')
# v_second = S.rindex('|')
# if v_first < s < v_second:
#     print('in')
# else:
#     print('out')
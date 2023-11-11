# # LRUD instruction 2

# N = int(input())
# S = input()


# l = [[0, 0]]

# # 初期位置
# x, y = 0, 0

# for i in range(N):
#     if S[i] == "R":
#         x += 1
#     elif S[i] == "L":
#         x -= 1
#     elif S[i] == "U":
#         y += 1
#     elif S[i] == "D":
#         y -= 1
    
#     if [x, y] in l:
#         print("Yes")
#         exit()
    
#     l.append([x, y])

# print('No')


N = int(input())
S = input()

# 複素数表記
pos = 0 + 0j

visited = set([pos])

for s in S:
    if s == "R":
        pos += 1
    elif s == "L":
        pos -= 1
    elif s == "U":
        pos += 1j
    else:
        pos -= 1j

    if pos in visited:
        print("Yes")
        exit()
    else:
        visited.add(pos)

print("No")

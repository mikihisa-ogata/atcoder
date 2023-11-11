# similar string

N = int(input())
S = input()
T = input()

answer = "Yes"

for i in range(N):
    if S[i] != T[i]:
        if S[i] == "o" and T[i] == "0":
            break
        if S[i] == "0" and T[i] == "o":
            break
        if S[i] == "1" and T[i] == "l":
            break
        if S[i] == "l" and T[i] == "1":
            break
        answer = "No"

print(answer)


# 解説

# def is_sim_char(c, d): # 
#     return (
#         c == d
#         or (c == "0" and d == "o")
#         or (c == "o" and d == "0")
#         or (c == "l" and d == "1")
#         or (c == "1" and d == "l")
#     )

# def is_sim_string(s, t):
#     for i in range(len(s)):
#         if not is_sim_char(s[i], t[i]):
#             return False
#     return True

# n = int(input())
# s = input()
# t = input()
# print("Yes" if is_sim_string(s, t) else "No")

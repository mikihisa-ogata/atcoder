# lookup

# S = input()
# T = input()

# for i in range(len(S) - len(T)):
#     if S[i: i + len(T)] == T:
#         print("Yes")
#         exit()

# print("No")

S = input()
T = input()
if T in S:
  print('Yes')
else:
  print('No')

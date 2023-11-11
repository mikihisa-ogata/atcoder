n_1 = int(input())
x = 0
y = 0
n = n_1
if n % 2 == 0:
  while n % 2 == 0:
    n = n//2
    x += 1
if n % 3 == 0:
  while n %3 == 0:
    n = n // 3
    y += 1

calc_n = (2 ** x) * (3 ** y)
if n_1 == calc_n:
  print("Yes")
else:
  print("No")


# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])

#     if temp!=1:
#         arr.append([temp, 1])

#     if arr==[]:
#         arr.append([n, 1])

#     return arr

# n = int(input())

# ans = factorization(n)
# print(ans)
# clac_n = 2 ** ans[0][1] * 3 ** ans[1][1]
# if ans[0][0] == 2 
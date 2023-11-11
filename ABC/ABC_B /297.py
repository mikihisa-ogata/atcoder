# chess960

S = input()
print(S)

l = []
for i in range(len(S)):
    l.append(S[i])

flag = False

def b_order(S):
  x = S.find('B')
  y = S.rfind('B')
  if (x + y) % 2 != 0 and (x*y)%2 == 0:
      return True

def rk(S):
  a = S.find('R')
  b = S.rfind('R')
  c = S.find('K')
  if a < c < b:
     return True

if b_order(S) and rk(S):
   print("Yes")
else:
   print('No')

# print(flag)
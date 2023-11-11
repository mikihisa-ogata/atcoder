n, m = map(int, input().split())
s = input()
t = input()

flag_1 = False
flag_2 = False

if t[:n] == s:
  flag_1 = True

if t[m-n:] == s:
  flag_2 = True

if flag_1 == True and flag_2 == True:
  print(0)
  exit()

if flag_1 == True and flag_2 == False:
  print(1)
  exit()

if flag_1 == False and flag_2 == True:
  print(2)
  exit()

if flag_1 == False and flag_2 == False:
  print(3)
  exit()
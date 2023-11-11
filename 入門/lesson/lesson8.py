
counter_C = 0

def judge_A(S):
  if S[0] =='A':
     return True

def judge_C(S):
  counter_C = 0
  for i in range(len(S)-2):
      if S[i+1] == 'C':
          counter_C +=1
  if counter_C == 1:
     return True

def judge_capital(S):
   for s in S:
      if s  != 'C' or 'A':
         if s != s.lower():
            break
   return True

S = str(input())

# if judge_A(S) and judge_C(S) and judge_capital(S):
#    print('AC')
# else:
#    print('WA')
if judge_A(S):
  #  print('A OK')
   if judge_C(S):
      # print('C OK')
      if judge_capital(S):
         print('AC')
      else:
         print('WA')
   else:
      print('WA')
else:
   print('WA')
   
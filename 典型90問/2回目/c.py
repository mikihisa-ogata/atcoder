import sys
import threading

sys.setrecursionlimit(67108864) #64MB
threading.stack_size(1024*1024)  #2の20乗のstackを確保=メモリの確保

k = int(input())
num = 0
cnt = 0

def like_num(num, cnt):
  x = [int(a) for a in str(num)]
  
  # 1桁の時
  if len(x) == 1:
    cnt += 1

  # 2桁の時
  else:
    flag = True
    for i in range(len(x) - 1):
     if x[i] <= x[i + 1]:
       flag = False
    
    if flag:
      cnt += 1

  num += 1

  if cnt == k:
    print(num)
    exit()
  else:
    like_num(num, cnt)

like_num(num, cnt)

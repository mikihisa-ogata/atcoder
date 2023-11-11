# fill the gaps

# n = int(input())
# a = []
# a.append(map(int, input().split()))
# print(a)

# b = a
# for i in range(n-1):
#     if abs(a[i] - a[i+1] == 1):
#         break
#     elif a[i] < a[i+1]:
#         b.append(list(range(a[i],a[i+1])))
#     else:
#         b.append(list(range(a[i+1],a[i])))

# print(b)

# 解説
input()
A=list(map(int,input().split()))
 
while True:
  if all(abs(A[i]-A[i+1])==1 for i in range(len(A)-1)):
    break
  for i in range(len(A)-1):
    if abs(A[i]-A[i+1])!=1:
      if A[i]<A[i+1]:
        A[i+1:i+1]=list(range(A[i]+1,A[i+1]))
      elif A[i]>A[i+1]:
        A[i+1:i+1]=list(range(A[i]-1,A[i+1],-1))
      break
 
print(*A)
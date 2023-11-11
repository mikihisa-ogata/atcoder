# the middle day

M = int(input())
D = list(map(int, input().split()))

days = []
sum = 0
for i in D:
    sum += i
    days.append(sum)

middle_day = int((sum + 1) / 2)

if M == 1:
   print(1, middle_day)

else:
   for i in range(M):
       if days[i] == middle_day:
          print(i + 1, D[i])
          exit()

       if days[i] < middle_day < days[i + 1]:
         print(i + 2,  middle_day - days[i])
         exit()


# elif M == 2:
#    for i in range(M):
#          if middle_day == days[i]:
#             print(i + 1, middle_day - days[i])

      #  if middle_day == days[i]:
      #     print(i + 1, middle_day - days[i])
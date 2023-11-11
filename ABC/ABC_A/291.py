# camel case

S = input()

for s in S:
    if s.isupper():
        print(S.find(s) + 1)
        break
    
# s=input()

# for i in range(len(s)):
#     if(s[i].isupper()):
#         print(i+1)

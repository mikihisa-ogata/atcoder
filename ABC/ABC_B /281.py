# sandwich number

S = input()
answer = "Yes"

if not len(S) == 8:
    answer = "No"
    
elif not S[0].isupper():
    answer = "No"

elif not S[7].isupper():
    answer = "No"

elif not S[1:7].isdigit():
    answer="No"

else:
    s = int(S[1:7])
    if not s >= 100000 and s <= 999999:
        answer = "No"

print(answer)

# s = input()
 
# if len(s) != 8 or s[0].isdigit() or s[7].isdigit():
#   print("No")
# elif not s[1:7].isdecimal() or s[1] == '0':
#   print("No")
# else:
#   print("Yes")
n = int(input())
s = input()

flag = False
for i in range(n - 1):
    if s[i] == "a" and s[i + 1] == "b" or s[i] == "b" and s[i + 1] == "a":
        flag = True

if flag:
    print("Yes")
else:
    print("No")

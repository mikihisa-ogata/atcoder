# flip

s = input()

output = ""
for i in range(len(s)):
    if s[i] == "0":
        output += "1"
    else:
        output += "0"

print(output)

# s = input()
# print(s.replace('0', 'x').replace('1', '0').replace('x', '1'))
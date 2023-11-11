# s = s.replace("ABC", "")
# s = s.replace("ABC", "")
# s = s.replace("ABC", "")
# print(s)
s = input()
n = 0
while n < len(s):
    # print(n, len(s), s)
    if s[n : n + 3] == "ABC":
        s = s.replace("ABC", "")
        n -= 3
    n += 1
print(s)

# for i in range(len(s)):
#     print(i, len(s))
#     if s[i : i + 3] == "ABC":
#         s = s.replace("ABC", "")
#         i -= 1

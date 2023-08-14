# PAST F double camel case sort

S = input()

words = []

i = 0
while i < len(S):
    # 初めてS[j]が大文字になるjを見つける
    j = i + 1
    while j < len(S) and S[j].islower():
        j += 1

    # 大文字の区間の文字列を抜き出してwordsに格納
    words.append(S[i:j + 1])

    # iを更新
    i = j + 1

words.sort(key=str.lower)
print("".join(words))
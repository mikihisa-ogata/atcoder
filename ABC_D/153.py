# caracal vs monster

H = int(input())
result = 0
count = 0
def rec(H, result, count):
    if H == 0:
        return result
    result += 2 ** count
    count += 1
    return rec(H // 2, result, count)

print(rec(H, result, count))
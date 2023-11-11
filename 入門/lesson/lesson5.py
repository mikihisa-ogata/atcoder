# N, A, B = map(int, input().split())

# n = 0
# l = 0
# for i in range(N):
#     if i < 10:
#         if A <= i <= B:
#             n += i
#     else:
#         while i >= 10:
#             l +=  i % 10
#             i //= 10
#         if A <= n <= B:
#             n += i

# ギブアップしました

# 解答例

def calc_sum_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    return sum_digit

N, A, B = map(int, input().split())

result = 0

for i in range(1, N+1):
    if A <= calc_sum_digit(i) <= B:
        result += i

print(result)
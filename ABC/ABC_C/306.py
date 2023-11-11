# centers

# n = int(input())
# a = list(map(int, input().split()))
# count = [ 0 for _ in range(n)]

# for i in range(3*n):
#     count[a[i]-1] += 1
#     if count[a[i]-1] == 2:
#         print(a[i], end=" ")

# 解答

n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(3 * n)]
ans = []
for i in a:
    cnt[i] += 1
    if cnt[i] == 2:
        ans.append(i)
print(*ans)
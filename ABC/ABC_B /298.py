# coloring matrix

N = int(input())
A = [list(map(int, input().split())) for l in range(N)]
B = [list(map(int, input().split())) for l in range(N)]

print(A)
print(B)

A = [list(a)[::-1] for a in zip(*A)] # Aの回転行列 たった1行で
print(A)
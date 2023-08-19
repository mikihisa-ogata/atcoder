from itertools import product

N = 3
for A in product(range(2), repeat=N):
    print(list(A))
from itertools import permutations

l = [1, 2, 3, 4]
L = permutations(l, 3)
for v in permutations(l, 3):
    print(v)
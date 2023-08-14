# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# transposed_A = list(zip(*A))

# print(A) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(transposed_A) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# print([list(a)[::-1] for a in zip(A)])
# print([list(a)[::-1] for a in zip(*A)]) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

a, b, *c = [1, 2, 3, 4, 5]
print(f'a={ a }')
print(f'b={ b }')
print(f'*c={ c }')
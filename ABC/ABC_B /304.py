# subscribes

n = int(input())

for i in range(7):
    if n < 10**(i+3):
        print(round(n, -1 * i))
        break
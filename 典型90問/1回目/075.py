# 075 - Magic For Balls

def prime_factorize(n):
    
    # 素因数を格納するリスト
    a = []

    # 2で割り続ける
    while n % 2 == 0:
        a.append(2)
        n //= 2
    
    # 3, 5, 7, ..., √n まで割り続ける
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        a.append(n)

    return a

n = int(input())

count = 0
while True:
    if len(prime_factorize(n)) <= 2 ** (count):
        print(count)
        exit()
    count += 1
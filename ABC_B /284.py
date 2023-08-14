# multi test cases

def count_odd(numbers, count=0):
    for number in numbers:
        if number % 2 == 1:
            count +=1
    return count

T = int(input())

result = []
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    result.append(count_odd(A))

for num in result:
    print(num)
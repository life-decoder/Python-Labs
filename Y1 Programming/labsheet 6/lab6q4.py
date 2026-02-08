from math import sqrt
start = int(input('start: '))
end = int(input('end: '))

for num in range(start, end + 1):
    isPrime = True
    for i in range(2, int(sqrt(num)) + 1):
        if ( num % i == 0):
            isPrime = False
            break
    if isPrime: print(num)

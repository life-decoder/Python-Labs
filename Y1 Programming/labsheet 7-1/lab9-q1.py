def factorial(n : int):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(eval(input('n: '))))

def power(x: float, n: int):
    return x ** n

def ratio(x: float, n: int):
    return power(x, n)/ factorial(n)

def sin(x : float):
    sum = 0
    for n in range(10):
        # print(power(-1, n))
        # print(power(x, 2*n + 1))
        # print(factorial(2*n + 1))
        sum += power(-1, n) * power(x, 2*n + 1) / factorial(2*n + 1)

    return sum
pi = 3.141592654
print(sin(pi / 6))
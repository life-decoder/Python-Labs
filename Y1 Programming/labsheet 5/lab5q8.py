x = float(input('Enter a real number: '))
n = int(input('Enter a positive integer: '))
y = 1
while (n > 0):
    y *= x
    n -= 1
print(f'{x}^{n} = {y}')
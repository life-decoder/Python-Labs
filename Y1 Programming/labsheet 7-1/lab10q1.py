def count_down(n : int):
    if n < 1:
        print("error")
    elif n > 1:
        print(n, end=' ')
        count_down(n - 1)
    else:
        print(1)

#count_down(int(input('n: ')))

def count_up(n : int):
    if n < 1:
        print("error")
    elif n > 1:
        count_up(n - 1)
        print('', n, end='')
    else:
        print(1, end='')

#count_up(int(input('n: ')))

def to_bin(num: int):
    if (num < 0):
        print('-', end='')
        to_bin(abs(num))
    elif num > 1:
        to_bin(num // 2)
        print(num % 2, end='')
    else:
        print(num, end='')

def add(x, y):
    if y == 0:
        return x
    else:
        return add(x + 1, y - 1)
    
print(add(int(input('x: ')), int(input('y: '))))
#to_bin(int(input('enter a decimal number: ')))
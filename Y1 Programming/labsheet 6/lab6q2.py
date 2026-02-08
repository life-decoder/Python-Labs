from math import sqrt
num = int(input("Enter a positive integer: "))
for i in range(1, num + 1):
    if (num % i == 0): print(i)
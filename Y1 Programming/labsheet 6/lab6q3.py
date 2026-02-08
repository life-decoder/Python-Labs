from math import sqrt
num = int(input("Enter a positive integer: "))
while (num < 1):
    num = int(input("Error! Try again: "))
isPrime = 'Prime'
for i in range(2, int(sqrt(num)) + 1):
    if (num % i == 0):
        isPrime = 'Not ' + isPrime
        break
print(isPrime)
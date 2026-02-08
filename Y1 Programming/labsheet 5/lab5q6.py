import random

num = random.randint(1, 100)
#print(num)
guess = int(input('Enter your guess (1-100): '))
while (guess != num):
    print('Wrong! ', end='')
    if (guess < 1 or guess > 100):
        print('The number should be between 1 and 100')
    elif (num < guess):
        print('The number is less than', guess)
    elif (num > guess):
        print('The number is greater than', guess)
    guess = int(input('Try another number: '))

print('Correct! The number is', num)
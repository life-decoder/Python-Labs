init_amount = float(input('Enter the initial investment: '))
interest = float(input('Enter the interest rate as a percentage: '))
curr_amount = init_amount
year = 0
while (curr_amount < 2 * init_amount):
    curr_amount *= (1 + interest / 100)
    print(curr_amount)
    year += 1

print(year)
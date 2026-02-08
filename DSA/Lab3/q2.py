def recursive_power(base, exp):
    if exp < 0:
        return 1 / base * recursive_power(base, exp + 1)
    if exp > 0:
        return base * recursive_power(base, exp - 1)
    else:
        return 1
    
print(recursive_power(int(input("Enter the base: ")), int(input("Enter the exponent: "))))

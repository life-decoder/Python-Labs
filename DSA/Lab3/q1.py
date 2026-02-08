def recursive_sum(num):
    if num <= 1:
        return num
    else:
        return num + recursive_sum(num - 1)
    

print(recursive_sum(int(input("Enter a positive integer: "))))
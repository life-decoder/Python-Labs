my_list = input("enter a list: ").split(",")
print(my_list)
i = 0
n = len(my_list) - 1
result = "symmetric"
while i <= int(n/2):
    if (my_list[i] != my_list[n - i]):
        result = "not " + result
        break
    i += 1
print(result)
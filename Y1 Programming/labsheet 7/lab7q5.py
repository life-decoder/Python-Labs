nums = []
while (True):
    num = input('enter num: ')
    if num == '':
        break
    else:
        nums.append(int(num))
print(nums)

print(min(nums), max(nums))

smallest = nums[0]
largest = nums[0]
for i in range(1, len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    if nums[i] < smallest:
        smallest = nums[i]

print('smallest:', smallest)
print('largest:', largest)
nums = list(range(1,11))
print(nums)
evens = 0
odds = 0
for num in nums:
    if (num % 2 == 0):
        evens += 1
    else:
        odds += 1
print(evens)
print(odds)
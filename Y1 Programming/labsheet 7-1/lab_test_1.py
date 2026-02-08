import random
count = [0] * 10
for i in range(100):
    count[random.randint(0, 99) // 10] += 1
# count = [0, 15, 10, 21, 38, 27, 31 , 14, 20, 6]
print("count:", count)
for level in range((max(count)// 10 + 1) * 10, 0, -10):
    for c in count:
        if c >= level:
            print(level, end='')
        elif c > level - 10:
            print(c % 10, end='')
        print(end='\t')
    print()
for i in range(10, 110, 10): print(f"<{i}", end='\t')
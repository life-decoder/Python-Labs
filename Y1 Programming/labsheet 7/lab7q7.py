listA = []
listB = []
n = int(input('enter a positive integer: '))
for i in range(n):
    listA.append(int(input('A - enter an integer: ')))
    listB.append(int(input('A - enter an integer: ')))
for numA, numB in zip(listA, listB):
    print(numA + numB)
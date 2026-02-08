"""
table = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f']
]
print(table)
"""
table = []
while True:
    row = input("enter row: ")
    if row == "":
        break
    else:
        table.append(row.split(","))

for row in table:
    for elmt in row:
        print(elmt.ljust(10), end='')
    print()


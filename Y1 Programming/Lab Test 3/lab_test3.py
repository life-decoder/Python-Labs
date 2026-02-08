count = [0] * 26
text_file = open("text.txt", 'r')
while True:
    char = text_file.read(1).lower()
    if char == '':
        break
    if char.isalpha():
        count[ord(char) - 97] += 1
text_file.close()
print(count)
for level in range((max(count)//10 + 1) * 10, 0, -10):
    for c in count:
        if c >= level:
            print(str(level).rjust(2, ' '), end='  ')
        elif c > level - 10:
            print(str(c % 10).rjust(2, ' '), end='  ')
        else:
            print('  ', end='  ')
    print()
for asc in range(ord('A'), ord('A') + 26):
    char = chr(asc)
    print(f"{char}{char.lower()}", end='  ')
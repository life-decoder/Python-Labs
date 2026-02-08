text = input('enter text: ')
word_count = 1
vowels = 'aeiou'
vowel_count = 0
for letter in text:
    if (letter == ' '):
        word_count += 1
    if letter.lower() in vowels:
        vowel_count += 1

print('number of words:', word_count)
print('number of vowels: ', vowel_count)
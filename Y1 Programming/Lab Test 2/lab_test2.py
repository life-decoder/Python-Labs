
def crypt(text_path: str, key_path: str, output_path: str, encrypt: bool = True):
	i, j = int(not encrypt), int(encrypt)
	with open(key_path, 'r') as key_file, open(text_path, 'r') as text_file:
		keys = [line.split('=') for line in key_file.read().split('\n')]
		text = [line.split() for line in text_file.read().split('\n')]
	print(keys), print(text)
	for line in range(len(text)):
		for word in range(len(text[line])):
			for key in keys:
				if (key[i] == text[line][word]):
					text[line][word] = key[j]
					break
		text[line] = ' '.join(text[line])
		print(text[line])
	with open(output_path, 'w') as output_file:
		output_file.write('\n'.join(text))
	if encrypt: crypt(output_path, key_path, 'test.txt', False)
crypt('plain.txt', 'key.txt', 'cipher.txt')
#crypt('cipher.txt', 'key.txt', 'decoded.txt', False) #To decode directly
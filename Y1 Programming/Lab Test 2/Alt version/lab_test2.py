text_path, key_path, output_path, i, j = "plain.txt", "key.txt", "cipher.txt", 0, 1
with open(key_path, 'r') as key_file:
	keys = [line.split('=') for line in key_file.read().split('\n')]
for _ in range(2):
	with open(text_path, 'r') as text_file:
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
	text_path, output_path, i, j = output_path, "reverse.txt", j, i
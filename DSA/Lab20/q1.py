""" 
Write a program that reads a small text file and applies the following pattern matching (string
searching) algorithms to search for some pattern provided as input by the user.
a. Brute-force algorithm
b. KMP algorithm
c. Boyer-Moore algorithm
You are required to count the number of comparisons made in each case and display the same in
a tabular format (for the same text file and the same search pattern).
"""


def brute_force_search(text, pattern):
	comparisons = 0
	text_length = len(text)
	pattern_length = len(pattern)

	if pattern_length == 0:
		return 0, comparisons

	for start in range(text_length - pattern_length + 1):
		for index in range(pattern_length):
			comparisons += 1
			if text[start + index] != pattern[index]:
				break
		else:
			return start, comparisons

	return -1, comparisons


def build_lps(pattern):
	lps = [0] * len(pattern)
	length = 0
	index = 1

	while index < len(pattern):
		if pattern[index] == pattern[length]:
			length += 1
			lps[index] = length
			index += 1
		elif length != 0:
			length = lps[length - 1]
		else:
			lps[index] = 0
			index += 1

	return lps


def kmp_search(text, pattern):
	comparisons = 0

	if not pattern:
		return 0, comparisons

	lps = build_lps(pattern)
	text_index = 0
	pattern_index = 0

	while text_index < len(text):
		comparisons += 1
		if text[text_index] == pattern[pattern_index]:
			text_index += 1
			pattern_index += 1

			if pattern_index == len(pattern):
				return text_index - pattern_index, comparisons
		else:
			if pattern_index != 0:
				pattern_index = lps[pattern_index - 1]
			else:
				text_index += 1

	return -1, comparisons


def build_bad_character_table(pattern):
	table = {}
	for index, character in enumerate(pattern):
		table[character] = index
	return table


def boyer_moore_search(text, pattern):
	comparisons = 0
	text_length = len(text)
	pattern_length = len(pattern)

	if pattern_length == 0:
		return 0, comparisons

	bad_character = build_bad_character_table(pattern)
	shift = 0

	while shift <= text_length - pattern_length:
		pattern_index = pattern_length - 1

		while pattern_index >= 0:
			comparisons += 1
			if pattern[pattern_index] != text[shift + pattern_index]:
				break
			pattern_index -= 1

		if pattern_index < 0:
			return shift, comparisons
		else:
			bad_character_index = bad_character.get(text[shift + pattern_index], -1)
			shift += max(1, pattern_index - bad_character_index)

	return -1, comparisons


def read_text_file(file_path):
	with open(file_path, "r", encoding="utf-8") as file:
		return file.read()


def print_results_table(results):
	headers = ["Algorithm", "First Occurrence Index", "Comparisons"]
	rows = [[name, str(index), str(comparisons)] for name, index, comparisons in results]

	widths = [len(header) for header in headers]
	for row in rows:
		for index, value in enumerate(row):
			widths[index] = max(widths[index], len(value))

	separator = "+" + "+".join("-" * (width + 2) for width in widths) + "+"
	header_row = "|" + "|".join(f" {headers[index].ljust(widths[index])} " for index in range(len(headers))) + "|"

	print(separator)
	print(header_row)
	print(separator)
	for row in rows:
		print("|" + "|".join(f" {row[index].ljust(widths[index])} " for index in range(len(row))) + "|")
	print(separator)


def get_default_text_and_pattern():
	return "ABABDABACDABABCABAB", "ABABCABAB"


def main():
	file_path = input("Enter the text file path: ").strip()
	pattern = input("Enter the search pattern: ").strip()
	default_text, default_pattern = get_default_text_and_pattern()

	if not file_path:
		text = default_text
		if not pattern:
			pattern = default_pattern
	else:
		try:
			text = read_text_file(file_path)
		except FileNotFoundError:
			print(f"File not found: {file_path}")
			return
		except OSError as error:
			print(f"Unable to read file: {error}")
			return

	if not pattern:
		pattern = default_pattern

	brute_force_index, brute_force_comparisons = brute_force_search(text, pattern)
	kmp_index, kmp_comparisons = kmp_search(text, pattern)
	boyer_moore_index, boyer_moore_comparisons = boyer_moore_search(text, pattern)

	print_results_table(
		[
			("Brute Force", brute_force_index, brute_force_comparisons),
			("KMP", kmp_index, kmp_comparisons),
			("Boyer-Moore", boyer_moore_index, boyer_moore_comparisons),
		]
	)


if __name__ == "__main__":
	main()
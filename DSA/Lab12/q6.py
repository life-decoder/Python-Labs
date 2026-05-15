"""
Using the same input arrays from Question 3, run each of the following algorithms and record
(1) the total comparisons, and (2) the runtime (using timeit):
- Selection sort
- Insertion sort
- Bubble sort
- Quicksort using rightmost element as pivot
- Quicksort using median-of-three method
"""

from __future__ import annotations

import random
import timeit


def selection_sort_count(arr):
	data = arr[:]
	comparisons = 0
	for i in range(len(data) - 1):
		min_index = i
		for j in range(i + 1, len(data)):
			comparisons += 1
			if data[j] < data[min_index]:
				min_index = j
		if min_index != i:
			data[i], data[min_index] = data[min_index], data[i]
	return comparisons


def insertion_sort_count(arr):
	data = arr[:]
	comparisons = 0
	for i in range(1, len(data)):
		key = data[i]
		j = i - 1
		while j >= 0:
			comparisons += 1
			if data[j] > key:
				data[j + 1] = data[j]
				j -= 1
			else:
				break
		data[j + 1] = key
	return comparisons


def bubble_sort_count(arr):
	data = arr[:]
	comparisons = 0
	for i in range(len(data) - 1):
		for j in range(len(data) - 1 - i):
			comparisons += 1
			if data[j] > data[j + 1]:
				data[j], data[j + 1] = data[j + 1], data[j]
	return comparisons


def quicksort_rightmost_count(arr):
	data = arr[:]

	def partition(left, right):
		nonlocal comparisons
		pivot = data[right]
		split = left
		for index in range(left, right):
			comparisons += 1
			if data[index] <= pivot:
				data[split], data[index] = data[index], data[split]
				split += 1
		data[split], data[right] = data[right], data[split]
		return split

	def quicksort(left, right):
		if left < right:
			pivot_index = partition(left, right)
			quicksort(left, pivot_index - 1)
			quicksort(pivot_index + 1, right)

	comparisons = 0
	if data:
		quicksort(0, len(data) - 1)
	return comparisons


def quicksort_median_of_three_count(arr):
	data = arr[:]

	def median_of_three(left, right):
		nonlocal comparisons
		middle = (left + right) // 2

		comparisons += 1
		if data[left] > data[middle]:
			left, middle = middle, left

		comparisons += 1
		if data[middle] > data[right]:
			middle, right = right, middle

		comparisons += 1
		if data[left] > data[middle]:
			left, middle = middle, left

		return middle

	def partition(left, right):
		nonlocal comparisons
		pivot_index = median_of_three(left, right)
		data[pivot_index], data[right] = data[right], data[pivot_index]
		pivot = data[right]
		split = left
		for index in range(left, right):
			comparisons += 1
			if data[index] <= pivot:
				data[split], data[index] = data[index], data[split]
				split += 1
		data[split], data[right] = data[right], data[split]
		return split

	def quicksort(left, right):
		if left < right:
			pivot_index = partition(left, right)
			quicksort(left, pivot_index - 1)
			quicksort(pivot_index + 1, right)

	comparisons = 0
	if data:
		quicksort(0, len(data) - 1)
	return comparisons


ALGORITHMS = [
	("Selection sort", selection_sort_count),
	("Insertion sort", insertion_sort_count),
	("Bubble sort", bubble_sort_count),
	("Quicksort (rightmost pivot)", quicksort_rightmost_count),
	("Quicksort (median-of-three)", quicksort_median_of_three_count),
]


def build_arrays(n):
	arrays = {
		"already sorted": list(range(n)),
		"reverse sorted": list(range(n - 1, -1, -1)),
		"random": list(range(n)),
	}
	random.shuffle(arrays["random"])
	return arrays


def benchmark(algorithm, arr, runs=1000):
	comparisons = algorithm(arr)
	elapsed = timeit.timeit(lambda: algorithm(arr), number=runs)
	return comparisons, elapsed / runs


def print_table(n, arrays):
	rows = []
	for algorithm_name, algorithm in ALGORITHMS:
		for input_name, arr in arrays.items():
			comparisons, seconds = benchmark(algorithm, arr)
			rows.append((algorithm_name, input_name, comparisons, seconds * 1000))

	headers = ["Algorithm", "Input type", "Comparisons", "Runtime (ms)"]
	widths = [len(header) for header in headers]
	for row in rows:
		widths[0] = max(widths[0], len(row[0]))
		widths[1] = max(widths[1], len(row[1]))
		widths[2] = max(widths[2], len(str(row[2])))
		widths[3] = max(widths[3], len(f"{row[3]:.6f}"))

	def line(left, fill, middle, right):
		return left + middle.join(fill * (width + 2) for width in widths) + right

	print(f"n = {n}")
	print(line("+", "-", "+", "+"))
	print(
		"| "
		+ " | ".join(
			[
				headers[0].ljust(widths[0]),
				headers[1].ljust(widths[1]),
				headers[2].rjust(widths[2]),
				headers[3].rjust(widths[3]),
			]
		)
		+ " |"
	)
	print(line("+", "-", "+", "+"))
	for algorithm_name, input_name, comparisons, runtime_ms in rows:
		print(
			"| "
			+ " | ".join(
				[
					algorithm_name.ljust(widths[0]),
					input_name.ljust(widths[1]),
					str(comparisons).rjust(widths[2]),
					f"{runtime_ms:.6f}".rjust(widths[3]),
				]
			)
			+ " |"
		)
	print(line("+", "-", "+", "+"))
	print()


def main():
	random.seed(0)
	for n in (50, 100):
		print_table(n, build_arrays(n))


if __name__ == "__main__":
	main()

"""
Question 2a:
Implement heapsort using an array-based heap.
"""


def heapify(values, heapSize, rootIndex):
	largest = rootIndex
	leftChild = 2 * rootIndex + 1
	rightChild = 2 * rootIndex + 2

	if leftChild < heapSize and values[leftChild] > values[largest]:
		largest = leftChild

	if rightChild < heapSize and values[rightChild] > values[largest]:
		largest = rightChild

	if largest != rootIndex:
		values[rootIndex], values[largest] = values[largest], values[rootIndex]
		heapify(values, heapSize, largest)


def heapSort(values):
	heapSize = len(values)

	for index in range(heapSize // 2 - 1, -1, -1):
		heapify(values, heapSize, index)

	for endIndex in range(heapSize - 1, 0, -1):
		values[0], values[endIndex] = values[endIndex], values[0]
		heapify(values, endIndex, 0)

	return values


def main():
	values = [12, 11, 13, 5, 6, 7]
	print("Original array:", values)
	print("Sorted array:", heapSort(values))


if __name__ == "__main__":
	main()

""" 
Question 1a:
Implement a priority queue using (1) a linked list, and (2) a heap.
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class PriorityQueueLinkedList:
	def __init__(self):
		self.front = None
		self.size = 0

	def isEmpty(self):
		return self.front is None

	def insert(self, element):
		newNode = Node(element)

		if self.isEmpty() or element > self.front.data:
			newNode.next = self.front
			self.front = newNode
		else:
			current = self.front
			while current.next is not None and current.next.data >= element:
				current = current.next
			newNode.next = current.next
			current.next = newNode

		self.size += 1

	def remove(self):
		if self.isEmpty():
			return -1

		removedElement = self.front.data
		self.front = self.front.next
		self.size -= 1
		return removedElement


class PriorityQueueHeap:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return len(self.queue) == 0

	def insert(self, element):
		self.queue.append(element)
		self._bubble_up(len(self.queue) - 1)

	def remove(self):
		if self.isEmpty():
			return -1

		removedElement = self.queue[0]
		lastElement = self.queue.pop()

		if not self.isEmpty():
			self.queue[0] = lastElement
			self._bubble_down(0)

		return removedElement

	def _bubble_up(self, index):
		parent = (index - 1) // 2

		while index > 0 and self.queue[index] > self.queue[parent]:
			self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
			index = parent
			parent = (index - 1) // 2

	def _bubble_down(self, index):
		size = len(self.queue)

		while True:
			leftChild = 2 * index + 1
			rightChild = 2 * index + 2
			largest = index

			if leftChild < size and self.queue[leftChild] > self.queue[largest]:
				largest = leftChild

			if rightChild < size and self.queue[rightChild] > self.queue[largest]:
				largest = rightChild

			if largest == index:
				break

			self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
			index = largest


def main():
	values = [2, 23, 12, 7, 13, 29, 50, 2, 23]

	print("Linked list priority queue:")
	linkedQueue = PriorityQueueLinkedList()
	for value in values:
		linkedQueue.insert(value)
	while not linkedQueue.isEmpty():
		print("Removed", linkedQueue.remove())

	print("\nHeap priority queue:")
	heapQueue = PriorityQueueHeap()
	for value in values:
		heapQueue.insert(value)
	while not heapQueue.isEmpty():
		print("Removed", heapQueue.remove())


if __name__ == "__main__":
	main()

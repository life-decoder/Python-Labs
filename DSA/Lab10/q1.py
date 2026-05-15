"""
You are required to implement (1) class HashTableEntry to store key and value pairs, (2) class
HashTable to keep a hash table of HashTableEntry objects and methods to manipulate the table, e.g.,
hashValue, put, remove, and get, and (3) a main program that will create a hash table and manipulate it.
"""


class HashTableEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value


class HashTable:
	def __init__(self, size=10):
		self.size = size
		self.table = [None] * size
		self._deleted = HashTableEntry(None, None)

	def hashValue(self, key):
		return hash(key) % self.size

	def put(self, key, value):
		index = self.hashValue(key)
		firstDeleted = None

		for _ in range(self.size):
			entry = self.table[index]

			if entry is None:
				if firstDeleted is not None:
					index = firstDeleted
				self.table[index] = HashTableEntry(key, value)
				return True

			if entry is self._deleted:
				if firstDeleted is None:
					firstDeleted = index
			elif entry.key == key:
				entry.value = value
				return True

			index = (index + 1) % self.size

		if firstDeleted is not None:
			self.table[firstDeleted] = HashTableEntry(key, value)
			return True

		return False

	def get(self, key):
		index = self.hashValue(key)

		for _ in range(self.size):
			entry = self.table[index]

			if entry is None:
				return -1

			if entry is not self._deleted and entry.key == key:
				return entry.value

			index = (index + 1) % self.size

		return -1

	def remove(self, key):
		index = self.hashValue(key)

		for _ in range(self.size):
			entry = self.table[index]

			if entry is None:
				return False

			if entry is not self._deleted and entry.key == key:
				self.table[index] = self._deleted
				return True

			index = (index + 1) % self.size

		return False

	def display(self):
		for index, entry in enumerate(self.table):
			if entry is None or entry is self._deleted:
				print(f"{index}: Empty")
			else:
				print(f"{index}: {entry.key} -> {entry.value}")


def main():
	hashTable = HashTable(10)

	print("Inserting items...")
	hashTable.put("apple", 50)
	hashTable.put("banana", 25)
	hashTable.put("orange", 75)
	hashTable.put("grape", 90)
	hashTable.display()

	print("\nLookup results:")
	print("apple =", hashTable.get("apple"))
	print("orange =", hashTable.get("orange"))
	print("pear =", hashTable.get("pear"))

	print("\nUpdating banana and removing grape...")
	hashTable.put("banana", 30)
	hashTable.remove("grape")
	hashTable.display()


if __name__ == "__main__":
	main()

import q1
import random

def quicksort_count(arr):
    """Use q1.quicksort to sort a copy and count element-vs-pivot comparisons."""
    a = arr[:]  # work on a copy
    counter = {'comps': 0}
    q1.quicksort(a, counter=counter, verbose=False)
    return counter['comps']

def main():
	random.seed(0)
	for n in (50, 100):
		arrays = {
			"already sorted": list(range(n)),
			"reverse sorted": list(range(n - 1, -1, -1)),
			"random": list(range(n))
		}
		random.shuffle(arrays["random"])
		print(f"n = {n}")
		for name, arr in arrays.items():
			comps = quicksort_count(arr)
			print(f"  {name:16s}: {comps} comparisons")
		print()

if __name__ == "__main__":
	main()
	_qs(0, len(a) - 1)
	return comps

def main():
	random.seed(0)
	for n in (50, 100):
		arrays = {
			"already sorted": list(range(n)),
			"reverse sorted": list(range(n - 1, -1, -1)),
			"random": list(range(n))
		}
		random.shuffle(arrays["random"])
		print(f"n = {n}")
		for name, arr in arrays.items():
			comps = quicksort_count(arr)
			print(f"  {name:16s}: {comps} comparisons")
		print()

if __name__ == "__main__":
	main()


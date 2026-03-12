""" Question 5
Implement an improved quicksort algorithm using:
a. Insertion sort for smaller sub-lists (let’s say list of size < 10)
b. Median-of-three method
"""


def insertion_sort(arr, left, right):
    """Sort a sublist of arr in place using insertion sort."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def median_of_three(arr, left, right):
    """Use median-of-three to choose a pivot and place it at right-1."""
    mid = (left + right) // 2
    # order left, mid, right
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    # place pivot at right-1
    arr[mid], arr[right - 1] = arr[right - 1], arr[mid]
    return arr[right - 1]


def improved_quicksort(arr, left=0, right=None):
    """Recursively sort arr using improved quicksort.

    Switches to insertion sort on small partitions and chooses pivot
    via median-of-three. This version sorts the list in place and
    returns the reference to the list for convenience.
    """
    if right is None:
        right = len(arr) - 1

    # base condition for recursion
    if left >= right:
        return arr

    # use insertion sort for small partitions
    if right - left + 1 < 10:
        insertion_sort(arr, left, right)
        return arr

    # choose pivot with median-of-three
    pivot = median_of_three(arr, left, right)
    i = left
    j = right - 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # restore pivot
    arr[i], arr[right - 1] = arr[right - 1], arr[i]

    improved_quicksort(arr, left, i - 1)
    improved_quicksort(arr, i + 1, right)
    return arr


if __name__ == "__main__":
    nums = [int(n) for n in input("Enter numbers to be sorted separated by space: ").split()]
    print("\nSorted:", improved_quicksort(nums))

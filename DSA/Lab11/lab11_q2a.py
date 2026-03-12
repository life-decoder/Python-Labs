""" Question 2
a. Implement the following sorting algorithms as a function:
- Selection sort
- Insertion sort
- Bubble sort

Each function must:
- Take a Python list myArray as input, and
- Return a new sorted list (do not modify the original list), sorted in ascending order
"""

def selection_sort(myArray):
    arr = myArray[:] # work on a copy
    #arr = myArray.copy()
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def insertion_sort(myArray):
    arr = myArray.copy() # work on a copy
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and key < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr

def bubble_sort(myArray):
    arr = myArray.copy() # work on a copy
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 90, 11, 22 ]
    print("Original array:", arr)
    print("Selection sorted:", selection_sort(arr))
    print("Insertion sorted:", insertion_sort(arr))
    print("Bubble sorted:", bubble_sort(arr))
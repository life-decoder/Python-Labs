""" Question 2b
Modify each algorithm in 2a so that it also counts:
- Number of comparisons: Every time two elements are compared (e.g., if a[i] > a[j])
- Number of exchanges: Every time two elements exchange positions
Each function must return (1) the sorted list, (2) the number of comparisons, and (3) the number
of exchanges.
"""

def selection_sort(myArray):
    """
    Sorts a list using Selection Sort and counts comparisons and exchanges.

    Args:
        myArray: The list to be sorted.

    Returns:
        A tuple containing:
        - The sorted list (a new list).
        - The number of comparisons.
        - The number of exchanges.
    """
    arr = myArray[:]
    comparisons = 0
    exchanges = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        # An exchange is a swap. Only swap if the found minimum is different.
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            exchanges += 1
    return arr, comparisons, exchanges

def insertion_sort(myArray):
    """
    Sorts a list using Insertion Sort and counts comparisons and element shifts.

    For this algorithm, an "exchange" is interpreted as an element shift,
    as elements are shifted to make space rather than being swapped directly.

    Args:
        myArray: The list to be sorted.

    Returns:
        A tuple containing:
        - The sorted list (a new list).
        - The number of comparisons.
        - The number of exchanges (element shifts).
    """
    arr = myArray[:]
    comparisons = 0
    exchanges = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements greater than key to the right
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                exchanges += 1
                j -= 1
            else:
                # Found the correct insertion point
                break
        arr[j + 1] = key
        
    return arr, comparisons, exchanges

def bubble_sort(myArray):
    """
    Sorts a list using Bubble Sort and counts comparisons and exchanges.

    Args:
        myArray: The list to be sorted.

    Returns:
        A tuple containing:
        - The sorted list (a new list).
        - The number of comparisons.
        - The number of exchanges.
    """
    arr = myArray[:]
    comparisons = 0
    exchanges = 0
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchanges += 1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, exchanges

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 90, 11, 22]
    
    print("Original array:", arr)
    
    sorted_arr_ss, comps_ss, exchs_ss = selection_sort(arr)
    print(f"\nSelection Sort:\n  Sorted: {sorted_arr_ss}\n  Comparisons: {comps_ss}, Exchanges: {exchs_ss}")
    
    sorted_arr_is, comps_is, exchs_is = insertion_sort(arr)
    print(f"\nInsertion Sort:\n  Sorted: {sorted_arr_is}\n  Comparisons: {comps_is}, Exchanges: {exchs_is} (shifts)")
    
    sorted_arr_bs, comps_bs, exchs_bs = bubble_sort(arr)
    print(f"\nBubble Sort:\n  Sorted: {sorted_arr_bs}\n  Comparisons: {comps_bs}, Exchanges: {exchs_bs}")
    
    print("\nOriginal array after all sorting functions:", arr)
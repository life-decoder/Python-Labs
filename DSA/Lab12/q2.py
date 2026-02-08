'''
Q2.
Modify your partition function so that it counts:
- How many times A[i] < v is evaluated,
- How many times A[j] >= v is evaluated.
Return the total number of comparisons per call to the partition function.
'''
def partition(arr, l, r):
    v = arr[r]
    i = l
    j = r
    count_lt_v = count_ge_v = 0
    while i < j:
        while (arr[i] < v):
            i += 1
            count_lt_v += 1
        count_lt_v += 1  # for the last failed comparison
        while (i < j) and (arr[j] >= v):
            j -= 1
            count_ge_v += 1
        count_ge_v += 1  # for the last failed comparison
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[i], arr[r] = arr[r], arr[i]
    return i, count_lt_v + count_ge_v
            

def quicksort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if r > l:
        i, count_comp = partition(arr, l, r)
        print("left:", arr[l:i], "\tpivot:", arr[i], "\tright:", arr[i+1:r + 1])
        print("Number of comparisons in this partition:", count_comp, end="\n\n")
        quicksort(arr, l, i - 1)
        quicksort(arr, i + 1, r)
    return arr


if __name__ == "__main__":
    nums = [int(n) for n in input("Enter numbers to be sorted separated by space: ").strip().split()]
    if not nums:
        nums = [5, 1, 8, 4, 2, 9, 7, 3, 6]
    print("Sorted:", quicksort(nums))
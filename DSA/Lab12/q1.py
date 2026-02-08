'''
Q1.
Implement the basic quicksort algorithm to sort numeric (integer) keys using the rightmost element
as the pivot (partitioning element). Your output should show the intermediate partitions created
during the sorting process.
'''
def partition(arr, l, r):
    v = arr[r]
    i = l
    j = r
    while i < j:
        while (arr[i] < v):
            i += 1
        while (i < j) and (arr[j] >= v):
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[i], arr[r] = arr[r], arr[i]
    return i
            

def quicksort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if r > l:
        i = partition(arr, l, r)
        print("left:", arr[l:i], "\tpivot:", arr[i], "\tright:", arr[i+1:r + 1])
        quicksort(arr, l, i - 1)
        quicksort(arr, i + 1, r)
    return arr


if __name__ == "__main__":
    nums = [int(n) for n in input("Enter numbers to be sorted separated by space: ").strip().split()]
    print("\nSorted:", quicksort(nums))
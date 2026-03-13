""" Question 2:
Implement each of the following search algorithms:
a. Linear Search
b. Binary Search (both the iterative and recursive versions)
c. Interpolation Search
d. Jump Search

This module provides implementations of the requested search routines.
Each function returns the index of the target in the list if found, or -1
if the target is not present.
"""

import math
from typing import List, Any, Optional


def linear_search(arr: List[Any], target: Any) -> int:
    """Perform a linear (sequential) search."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search_iterative(arr: List[Any], target: Any) -> int:
    """Iterative binary search. Assumes `arr` is sorted."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(
    arr: List[Any], target: Any, lo: int = 0, hi: Optional[int] = None
) -> int:
    """Recursive binary search. Assumes `arr` is sorted."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)


def interpolation_search(arr: List[float], target: float) -> int:
    """Interpolation search for uniformly distributed, sorted numeric data."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if lo == hi:
            return lo if arr[lo] == target else -1
        # estimate the position
        pos = lo + int(
            (target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo])
        )
        # guard array bounds
        if pos < lo or pos > hi:
            break
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


def jump_search(arr: List[Any], target: Any) -> int:
    """Jump search using block size sqrt(n)."""
    n = len(arr)
    if n == 0:
        return -1
    step = int(math.sqrt(n))
    prev = 0
    # find the block where target may be
    while prev < n and arr[min(n - 1, prev + step - 1)] < target:
        prev += step
    # linear search within block
    for i in range(prev, min(prev + step, n)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    # simple demonstration / smoke tests
    sample = list(range(0, 50, 5))
    targets = [0, 25, 45, 47]
    print("array:", sample)
    for t in targets:
        print(f"searching {t}:")
        print(" linear ->", linear_search(sample, t))
        print(" binary (iter) ->", binary_search_iterative(sample, t))
        print(" binary (rec) ->", binary_search_recursive(sample, t))
        print(" interpolation ->", interpolation_search(sample, t))
        print(" jump ->", jump_search(sample, t))

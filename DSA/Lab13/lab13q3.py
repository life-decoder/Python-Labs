""" Create modified versions of the functions for each algorithm in Question 2 so that it also returns the number of
comparisons made. """

import math
from typing import Any, List, Optional, Tuple


def linear_search(arr: List[Any], target: Any) -> Tuple[int, int]:
    """Linear search, returns (index, comparisons)."""
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons += 1  # value == target
        if value == target:
            return i, comparisons
    return -1, comparisons


def binary_search_iterative(arr: List[Any], target: Any) -> Tuple[int, int]:
    """Iterative binary search, returns (index, comparisons)."""
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        comparisons += 1
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comparisons


def binary_search_recursive(
    arr: List[Any],
    target: Any,
    lo: int = 0,
    hi: Optional[int] = None,
    comparisons: int = 0,
) -> Tuple[int, int]:
    """Recursive binary search, returns (index, comparisons)."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1, comparisons
    mid = (lo + hi) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    comparisons += 1
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi, comparisons)
    return binary_search_recursive(arr, target, lo, mid - 1, comparisons)


def interpolation_search(arr: List[float], target: float) -> Tuple[int, int]:
    """Interpolation search, returns (index, comparisons)."""
    lo = 0
    hi = len(arr) - 1
    comparisons = 0
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        comparisons += 2  # bounds checks arr[lo] <= target and target <= arr[hi]

        if lo == hi:
            comparisons += 1
            return (lo, comparisons) if arr[lo] == target else (-1, comparisons)

        pos = lo + int((target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]))
        if pos < lo or pos > hi:
            comparisons += 1
            break

        comparisons += 1
        if arr[pos] == target:
            return pos, comparisons

        comparisons += 1
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1, comparisons


def jump_search(arr: List[Any], target: Any) -> Tuple[int, int]:
    """Jump search, returns (index, comparisons)."""
    n = len(arr)
    if n == 0:
        return -1, 0
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0
    while prev < n:
        current = min(n - 1, prev + step - 1)
        comparisons += 1
        if arr[current] >= target:
            break
        prev += step
    for i in range(prev, min(prev + step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


if __name__ == "__main__":
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

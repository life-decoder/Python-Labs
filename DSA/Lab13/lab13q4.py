""" Create an array of size 1000 with:
a. Random values
b. Uniformly distributed values (you may use the uniform() method from random module)
c. Skewed values (many small numbers and a few large numbers)
Run each of the search algorithms on each array from q2 """

import random
import time
from typing import List, Any

from lab13q2 import (
    linear_search,
    binary_search_iterative,
    binary_search_recursive,
    interpolation_search,
    jump_search,
)


def generate_random_array(size: int) -> List[int]:
    return [random.randint(0, 10000) for _ in range(size)]


def generate_uniform_array(size: int) -> List[float]:
    return [random.uniform(0, 10000) for _ in range(size)]


def generate_skewed_array(size: int) -> List[int]:
    arr = [random.randint(0, 100) for _ in range(int(size * 0.9))]
    arr += [random.randint(10000, 100000) for _ in range(size - len(arr))]
    random.shuffle(arr)
    return arr


def time_search(func, arr: List[Any], target: Any) -> float:
    start = time.perf_counter()
    idx = func(arr, target)
    end = time.perf_counter()
    return (end - start) * 1e6, idx


def run_all_searches(arr: List[Any], target: Any, sorted_required: bool = False):
    print(f"\nTarget = {target}")
    if sorted_required:
        arr2 = sorted(arr)
    else:
        arr2 = arr

    probes = []
    probes.append(("linear_search", linear_search, arr2, target))
    probes.append(("binary_search_iterative", binary_search_iterative, arr2, target))
    probes.append(("binary_search_recursive", binary_search_recursive, arr2, target))
    probes.append(("jump_search", jump_search, arr2, target))
    # interpolation_search expects numeric sorted list
    if all(isinstance(x, (int, float)) for x in arr2):
        probes.append(("interpolation_search", interpolation_search, arr2, target))

    for name, func, array, targ in probes:
        duration, idx = time_search(func, array, targ)
        print(f" {name:25}: index={idx:4} time={duration:8.2f}µs")


def summarize_array(name: str, arr: List[Any]):
    print(f"\n=== {name} (size={len(arr)}) ===")
    for t in [arr[0], arr[len(arr) // 2], arr[-1], random.choice(arr)]:
        run_all_searches(arr, t, sorted_required=True)


if __name__ == "__main__":
    SIZE = 1000

    random.seed(0)
    random_arr = generate_random_array(SIZE)
    uniform_arr = generate_uniform_array(SIZE)
    skewed_arr = generate_skewed_array(SIZE)

    print("Search comparison on different distributions")

    summarize_array("Random array", random_arr)
    summarize_array("Uniform array", uniform_arr)
    summarize_array("Skewed array", skewed_arr)

    # test lookups for non-existing values
    for arr_name, arr in [
        ("Random array", random_arr),
        ("Uniform array", uniform_arr),
        ("Skewed array", skewed_arr),
    ]:
        not_found_target = 9999999
        print(f"\n{name} not found target eval")
        run_all_searches(arr, not_found_target, sorted_required=True)

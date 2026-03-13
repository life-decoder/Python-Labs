"""The Fibonacci sequence is defined as:
Fib(0) = 0
Fib(1) = 1
Fib(n) = Fib(n - 1) + Fib(n - 2) for n > 1

a. Implement a recursive function that takes an integer value, n, as argument, and
computes and returns the nth Fibonacci number in the sequence.

b. Implement a function that computes and returns the nth Fibonacci number using
   dynamic programming.
"""

from __future__ import annotations


def fib_recursive(n: int) -> int:
    """Return the nth Fibonacci number using recursion.

    This implementation directly follows the definition:
      Fib(0) = 0
      Fib(1) = 1
      Fib(n) = Fib(n-1) + Fib(n-2)

    Note: This is exponential-time and is intended only for small n.
    """

    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dynamic(n: int) -> int:
    """Return the nth Fibonacci number using dynamic programming.

    This implementation computes values iteratively and stores previous results,
    resulting in linear time and constant space.
    """

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def _test():
    """Quick sanity checks for both implementations."""

    test_values = [0, 1, 2, 3, 5, 10, 20]
    print("n | recursive | dynamic")
    print("--+-----------+--------")
    for n in test_values:
        print(f"{n:2d} | {fib_recursive(n):9d} | {fib_dynamic(n):7d}")


if __name__ == "__main__":
    _test()

"""Fractional Knapsack (Greedy)

Reads:
 - n (number of items)
 - W (knapsack capacity)
 - n lines, each with: weight value

Outputs:
 - fraction of each item taken (in original order)
 - total weight taken
 - total value (benefit) achieved

Example input:
3 50
10 60
20 100
30 120

Example output:
Fractions: [1.0, 1.0, 0.6666666666666666]
Total weight: 50.0
Total value : 240.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Item:
    index: int
    weight: float
    value: float


def fractional_knapsack(capacity: float, items: List[Item]) -> Tuple[List[float], float, float]:
    """Return (fractions, total_weight, total_value).

    Fractions are returned in the original order of the items list.
    """

    # Sort items by value/weight ratio descending (greedy choice)
    items_sorted = sorted(
        items, key=lambda it: it.value / it.weight if it.weight > 0 else 0.0, reverse=True
    )

    fractions = [0.0] * len(items)
    total_weight = 0.0
    total_value = 0.0

    remaining = capacity
    for it in items_sorted:
        if remaining <= 0:
            break
        if it.weight <= remaining:
            take = 1.0
        else:
            take = remaining / it.weight

        fractions[it.index] = take
        total_weight += take * it.weight
        total_value += take * it.value
        remaining -= take * it.weight

    return fractions, total_weight, total_value


def _parse_input() -> Tuple[float, List[Item]]:
    data = input().strip().split()
    if len(data) < 2:
        raise ValueError("Expected at least two values: n and W")

    n = int(data[0])
    capacity = float(data[1])

    items: List[Item] = []

    # If remaining tokens already include item data, consume them; else read lines.
    tokens = data[2:]
    while len(items) < n:
        if len(tokens) < 2:
            line = input().strip()
            if not line:
                continue
            tokens = line.split()
        if len(tokens) < 2:
            raise ValueError("Expected weight and value for each item")
        weight = float(tokens[0])
        value = float(tokens[1])
        items.append(Item(index=len(items), weight=weight, value=value))
        tokens = tokens[2:]

    return capacity, items


def main() -> None:
    try:
        capacity, items = _parse_input()
    except Exception as e:
        print(f"Error reading input: {e}")
        return

    fractions, total_weight, total_value = fractional_knapsack(capacity, items)

    print("Fractions:", fractions)
    print(f"Total weight: {total_weight}")
    print(f"Total value : {total_value}")


if __name__ == "__main__":
    main()

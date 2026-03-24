"""Define a function that, given a set of coin denominations and a target amount, determines the
minimum number of coins required to make the amount using:

a. A Greedy approach
b. A Recursive approach
c. A Dynamic Programming approach

Test your function with different input and compare the results of the different approaches.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

def greedy_coin_change(denominations: Iterable[int], amount: int) -> Optional[int]:
    """Return the minimum number of coins to make `amount` using a greedy strategy.

    The greedy algorithm picks the largest denomination coin available at each step.
    This is not guaranteed to be optimal for all denomination sets (non-canonical systems),
    but works correctly for common systems like U.S. coins.

    Returns None if the amount cannot be made from the given denominations.
    """

    if amount < 0:
        return None

    coins = sorted((d for d in denominations if d > 0), reverse=True)
    if not coins:
        return None

    remaining = amount
    count = 0

    for coin in coins:
        if remaining <= 0:
            break
        use = remaining // coin
        if use > 0:
            count += use
            remaining -= use * coin

    return count if remaining == 0 else None


def recursive_coin_change(denominations: Iterable[int], amount: int) -> Optional[int]:
    """Compute minimum number of coins to make `amount` using recursion (top-down).

    This implementation uses memoization to avoid exponential blow-up.
    Returns None if the amount cannot be made.
    """

    coins = sorted([d for d in denominations if d > 0])
    if amount < 0 or not coins:
        return None

    memo: dict[int, Optional[int]] = {0: 0}

    def _min_coins(remaining: int) -> Optional[int]:
        if remaining < 0:
            return None

        if remaining in memo:
            return memo[remaining]

        best: Optional[int] = None
        for coin in coins:
            if coin > remaining:
                break
            sub = _min_coins(remaining - coin)
            if sub is None:
                continue
            candidate = sub + 1
            if best is None or candidate < best:
                best = candidate

        memo[remaining] = best
        return best

    return _min_coins(amount)


def dp_coin_change(
    denominations: Iterable[int], amount: int
) -> Tuple[Optional[int], Optional[List[int]]]:
    """Compute minimum number of coins to make `amount` using dynamic programming (bottom-up).

    Returns a tuple (min_coins, coins_used).
    If the amount cannot be made, returns (None, None).
    """

    coins = sorted([d for d in denominations if d > 0])
    if amount < 0 or not coins:
        return None, None

    # dp[i] = minimum coins needed to make amount i, or None if impossible
    dp: List[Optional[int]] = [None] * (amount + 1)
    dp[0] = 0

    # best_coin[i] = coin denomination used to reach the optimal solution for amount i
    best_coin: List[Optional[int]] = [None] * (amount + 1) # For traceback

    for value in range(1, amount + 1):
        best: Optional[int] = None
        best_choice: Optional[int] = None # For traceback
        for coin in coins:
            if coin > value:
                break
            if dp[value - coin] is None:
                continue
            candidate = dp[value - coin] + 1
            if best is None or candidate < best:
                best = candidate
                best_choice = coin # For traceback
        dp[value] = best
        best_coin[value] = best_choice # Store the coin used for the optimal solution at this value

    if dp[amount] is None:
        return None, None

    # Traceback to reconstruct used coins
    used: List[int] = []
    remaining = amount
    while remaining > 0:
        coin = best_coin[remaining]
        assert coin is not None  # type-checker; should never happen when dp[amount] is set
        used.append(coin)
        remaining -= coin

    return dp[amount], used


def _run_test(
    denominations: Iterable[int], amount: int
) -> Tuple[Optional[int], Optional[int], Optional[int], Optional[List[int]]]:
    greedy = greedy_coin_change(denominations, amount)
    rec = recursive_coin_change(denominations, amount)
    dp_count, dp_coins = dp_coin_change(denominations, amount)
    return greedy, rec, dp_count, dp_coins


if __name__ == "__main__":
    test_cases = [
        ((1, 5, 10, 25), 63),
        ((1, 3, 4), 6),  # non-canonical system where greedy is not optimal (greedy gives 3+3 = 2 coins, actually optimal is 3+3? this is fine)
        ((1, 3, 4), 7),  # non-canonical: greedy gives 4+1+1+1 = 4 coins, optimal is 3+4 = 2 coins
        ((2, 5, 10), 7),  # impossible
    ]

    for coins, amount in test_cases:
        greedy, rec, dp_count, dp_coins = _run_test(coins, amount)
        print(f"coins={coins} amount={amount}")
        print(f"  greedy => {greedy}")
        print(f"  recursive => {rec}")
        print(f"  dp => {dp_count}")
        if dp_coins is not None:
            print(f"    coins used (dp) => {dp_coins}")
        print()

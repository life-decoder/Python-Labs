from timeit import timeit
def sum_loop(n):
    sum = 0
    while (n > 0):
        sum += n
        n -= 1
    return sum

def sum_formula(n):
    return n * (1 + n) / 2

n = 100
exec_time = timeit("sum_loop(n)", "from __main__ import sum_loop, n", number=500)
print("Loop:")
print(f"Total time for 500 runs: {exec_time:.6f} seconds")
print(f"Average time per run: {exec_time/500:.8f} seconds")

exec_time = timeit("sum_formula(n)", "from __main__ import sum_formula, n", number=500)
print("\nFormula:")
print(f"Total time for 500 runs: {exec_time:.6f} seconds")
print(f"Average time per run: {exec_time/500:.8f} seconds")
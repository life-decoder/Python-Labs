from timeit import timeit
# function to test
def sum_of_squares(n):
    return sum(x**2 for x in range(n))
    # test parameters
n = 1000
    # measure execution time over 500 runs
execution_time = timeit(stmt="sum_of_squares(n)",setup="from __main__ import sum_of_squares, n",number=500)

print(f"Total time for 500 runs: {execution_time:.6f} seconds")
print(f"Average time per run: {execution_time/500:.8f} seconds")


memo = {}

def count(n, m):
    if n < 1 or m < 1:
        return 0
    if n < m or n == 1 or m == 1:
        return 1
    if n == m:
        return 2

    if (n, m) in memo:
        print(f"Memoized result for {n}x{m} is", memo[(n, m)])
        return memo[(n, m)]

    result = count(n-1, m) + count(n-m, m) # * count(m, m-1)
    print(f"Calculated result for {n}x{m} is", result)
    memo[(n, m)] = result

    return result

if __name__ == "__main__":
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    print(count(n, m))

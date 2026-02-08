def q2():
    def binary_strings(n, s = ""):
        if len(s) > 1 and s[-2:] == "11":
            return []
        if n == 0:
            return [s]
        return binary_strings(n-1, s + '1') + binary_strings(n-1, s + '0')

    def binary_strings_alt(n, s, result):
        """         
        Given an integer value num, where 1 ≤ num ≤ 20, generate all binary strings of length num that do not
        contain "11".
        As an example, suppose that n = 3, the output will be 000, 001, 010, 100 and 101.
        """
        if len(s) > 1 and s[-2:] == "11":
            return
        if n == 0:
            result.append(s)
            return
        binary_strings_alt(n-1, s + '0', result)
        binary_strings_alt(n-1, s + '1', result)

    print("Binary strings of length 3:", binary_strings(3), end="\n\n")

    result = []
    binary_strings_alt(3, "", result)
    print("Binary strings of length 3 (alternative):", result, end="\n\n")

def q1():
    '''
    Given an array of n positive integers and a value num, print any one subset whose sum is exactly num, or report "No solution".
    As an example, suppose that the array is [3, 4, 5, 2] and num = 9. One answer is [4, 5]. Many others may also exist.
    Implement the solution using backtracking.
    '''
    def backtrack(arr, target, start, current_subset):
        # Base case: if target is 0, we found a solution
        if target == 0:
            return current_subset[:]
        
        # Base case: if target becomes negative or we've exhausted all elements
        if target < 0 or start >= len(arr):
            return None
        
        # Try including the current element
        current_subset.append(arr[start])
        result = backtrack(arr, target - arr[start], start + 1, current_subset)
        if result is not None:
            return result
        current_subset.pop()  # Backtrack
        
        # Try excluding the current element
        result = backtrack(arr, target, start + 1, current_subset)
        return result

    # Test with the example
    arr = [3, 4, 5, 2]
    num = 9

    result = backtrack(arr, num, 0, [])

    if result is not None:
        print(f"Array: {arr}, Target: {num}")
        print(f"Solution: {result}")
    else:
        print("No solution")

if __name__ == "__main__":
    q1()